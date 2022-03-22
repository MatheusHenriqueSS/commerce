from re import search
from django.contrib import admin
from .models import User, Listing, Bid, Comment, Watchlist, Category

# Register your models here.
admin.site.register(User)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'listing', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'category', 'active', 'date', 'user')
    list_filter = ('active', 'date', 'category', 'user')
    search_fields = ('product', 'category', 'user__username')

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('user', 'auction', 'price', 'valid', 'date')
    list_filter = ('valid', 'date', 'auction', 'user')
    search_fields = ('user__username', 'auction__product')

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'item')
    list_filter = ('user', 'item')
    search_fields = ('user__username', 'item__product')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)