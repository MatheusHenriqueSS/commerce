from queue import Empty
from django.contrib.auth import authenticate, login, logout, get_user
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


from .models import User, Listing, Watchlist, Bid, Category
from .forms  import CreateListing, CommentForm


def index(request):
    listing = Listing.objects.filter(active=True)
    
    message = ""
    if listing is None or len(listing) == 0:
        message = f"<div class=\"alert alert-secondary text-center\">There is no active auction.</div>"

    return render(request, "auctions/index.html", {"title": "Active Listings", "query": listing, "message": message})

@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        form = CreateListing(request.POST)
        print(form.errors)
        if form.is_valid():
            bidding_value = form.cleaned_data.get("price")
            bidding_value = bidding_value.replace(',', "").replace('.', "")    
            bidding_value = round(int(bidding_value) / 100, 2)
            print(form.cleaned_data.get("category"))
            new_entry = Listing(product=form.cleaned_data.get("product"), price=bidding_value, image=form.cleaned_data.get("image"), description=form.cleaned_data.get("description"), category=Category.objects.get(name=form.cleaned_data.get("category")), user=get_user(request))
            new_entry.save()
            return HttpResponseRedirect(reverse("listing", kwargs={"product": new_entry.id}))
    else:
        form = CreateListing()
    return render(request, "auctions/create.html", {"form": form, "categories": categories}) 


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def listing(request, product):
    is_logged = request.user.is_authenticated
    is_active = Listing.objects.get(id=product).active
    
    # if (is_active == False):
    #     return HttpResponseRedirect(reverse("checkout", kwargs={"product": product}))

    highest_bid = Bid.objects.filter(auction=Listing.objects.get(id=product), valid=True).order_by('-price').first()
    if (highest_bid is not None):
        Listing.objects.filter(id=product).update(price = highest_bid.price)
    
    listing = Listing.objects.filter(id=product).first()
    
    is_creator = False
    creator = None
    if (is_logged):
        creator = Listing.objects.filter(id = product, user=User.objects.get(id=get_user(request).id)).first()

    if creator is not None:
        is_creator = True

    on_watchlist = False
    watchlist = None
    if (is_logged):
        watchlist = Watchlist.objects.filter(item = product, user=User.objects.get(id=get_user(request).id)).first()
    
    if watchlist is not None:
        on_watchlist = True
    
    #alert error bidding

    #last_bid = Bid.objects.filter(auction = product, user = User.objects.get(id=get_user(request).id)).order_by('-date').first()

    message = ""
    if is_logged == True:
        last_bid = Bid.objects.filter(auction = product, user = User.objects.get(id=get_user(request).id)).order_by('-date').first()
        if last_bid is not None and last_bid.valid == False and last_bid.alert == False:
            last_bid.alert = True
            last_bid.save()
            message = "<div class=\"alert alert-danger text-center\">Bid not accepted: The price has increased</div>"
        elif last_bid is not None and last_bid.valid == True and last_bid.alert == False and last_bid.price == listing.price:
            last_bid.alert = True
            last_bid.save()
            message = "<div class=\"alert alert-success text-center\"> Bid accepted: Your bid is the current bid</div>"

    #comment section handling

    comments = listing.comments.filter(active=True)
    new_comment = None


    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            
            # create comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            if new_comment.body == "":
                #handle empty commentary
                new_comment = None
            else:
            # assign the current post to the comment and the creator username
                new_comment.listing = listing
                new_comment.name = get_user(request).username
                # save the comment to the database
                new_comment.save()
    
    comment_form = CommentForm()

    #auction closed mensage handling

    creator = Listing.objects.get(id=product).user
    winner_bid = Bid.objects.filter(auction=Listing.objects.get(id=product), valid=True).order_by('-price').first()

    winner=""
    if (winner_bid is not None):
        #the auction had no valid bids
        winner = winner_bid.user
        winner_bid = winner_bid.price

    current_user = get_user(request)

    main_msg=""
    if winner == "":
        main_msg = f"The auction had no winners."
    elif (current_user.id == creator.id):
        main_msg = f"You finished the auction. {winner.username} won the auction with a winner bid of ${winner_bid:,}."
    elif (current_user.id == winner.id):
        main_msg = f"Congratulations! You won the auction with a winner bid of ${winner_bid:,}."
    elif current_user.id != winner.id and current_user.id != creator.id:
        main_msg = f"The auction has been closed." 


    
    return render(request, "auctions/listing.html", {"q": listing, "on_watchlist": on_watchlist, 
    "auction_id": product, "is_creator": is_creator, "comments": comments, "new_comment": new_comment,
     "comment_form": comment_form, "message": message, "main_msg": main_msg})

@csrf_exempt
def watchlist(request):
    if request.method == "POST":
        auction_id = request.POST["auction_id"]
        watchlist_item = Watchlist.objects.filter(item=auction_id, user=User.objects.get(id=get_user(request).id)).first()

        if watchlist_item is not None:
            #remove item from watchlist
            watchlist_item.delete()
        else:   
            #save item in watchlist
            new_entry = Watchlist(item=Listing.objects.get(id=auction_id), user = User.objects.get(id=get_user(request).id))
            new_entry.save()
        return HttpResponse("Sucess!")
    else:
        return HttpResponse("Request method is not a POST")


def close_listing(request):
    if request.method == "POST":
        auction_id = request.POST["auction_id"]
        Listing.objects.filter(id = auction_id).update(active=False)

        return HttpResponseRedirect(reverse("listing", kwargs={"product": auction_id}))


def checkout(request, product):

    winner_username = ""
    if winner != "":
        winner_username = winner.username
    return render(request, "auctions/checkout.html", {"creator_username": creator.username, "winner_username": winner_username, "main_msg": message})

def bid(request):
    bidding_value = request.POST["bidding_val"]
    auction_id = request.POST["auction_id"]
    current_value = Listing.objects.get(id=auction_id).price
    is_active = Listing.objects.get(id=auction_id).active

    if (is_active == False):
        return HttpResponseRedirect(reverse("checkout", kwargs={"product": auction_id}))
    

    bidding_value = bidding_value.replace(',', "").replace('.', "")    
    bidding_value = round(int(bidding_value) / 100, 2)
    bidding_validation = True
    if (bidding_value <= float(current_value)):
        bidding_validation = False

    new_entry = Bid(price=bidding_value, auction=Listing.objects.get(id=auction_id), user=User.objects.get(id=get_user(request).id), valid=bidding_validation)
    new_entry.save()

    return HttpResponseRedirect(reverse("listing", kwargs={"product": auction_id}))

@login_required(login_url='login')
def watchlist_page(request):
    watchlist = Listing.objects.filter(active = True, watchlist__user=get_user(request).id)

    message = ""
    if watchlist is None or len(watchlist) == 0:
        message = f"<div class=\"alert alert-info text-center\"> Your watchlist is empty!</div>"
    return render(request, "auctions/index.html", {"title": "Watchlist", "query": watchlist, "message": message})

def categories(request):
    categories = Category.objects.filter()
    return render(request, "auctions/categories.html", {"q": categories})

def category(request, type):
    listing = Listing.objects.filter(active = True, category=Category.objects.get(name=type))
    
    message = ""
    if listing is None or len(listing) == 0:
        message = f"<div class=\"alert alert-info text-center\"> There is no active auction for {type}.</div>"
    return render(request, "auctions/index.html", {"title": type.capitalize(), "query": listing, "message": message})

@login_required(login_url='login')
def my_listings(request):
    listing = Listing.objects.filter(user=User.objects.get(id=get_user(request).id))

    message = ""
    if listing is None or len(listing) == 0:
         message = f"<div class=\"alert alert-info text-center\"> You have not created any auction yet.</div>"
    return render(request, "auctions/index.html", {"title": "My listings", "query": listing, "message": message, "my_listings": True})


@csrf_exempt
def on_watchlist(request):
    if request.method == "POST":
        product_id = request.POST["product_id"] 
        watchlist_item = Watchlist.objects.filter(item = product_id, user = User.objects.get(id=get_user(request).id)).first()

        if watchlist_item is not None:
            return HttpResponse("1")
        else:
            return HttpResponse("0")
    else:
        return HttpResponse("Request method is not a POST")

@csrf_exempt
def current_price(request):
    if request.method == "POST":
        product_id = request.POST["product_id"]
    
        listing = Listing.objects.filter(id=product_id).first()

        print(listing.price)
        return HttpResponse(listing.price)
    else:
        return HttpResponse("Request method is not a POST")
        