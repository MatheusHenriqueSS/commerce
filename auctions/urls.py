from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listings/<str:product>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("close", views.close_listing, name="close"),
    path("bid", views.bid, name="bid"),
    path("watchlists", views.watchlist_page, name="watchlist_page"),
    path("categories", views.categories, name="categories"),
    path("category/<str:type>", views.category, name="category"),
    path("my_listings", views.my_listings, name="my_listings"),
    path("on_watchlist", views.on_watchlist, name="on_watchlist"),
    path("current_price", views.current_price, name="current_price"),
    path("is_active", views.is_active, name="is_active")
]
