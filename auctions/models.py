from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils.timezone import now


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=100, null = True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Listing(models.Model):
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=5000, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None)
    description = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(default=now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product

class Bid(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    date = models.DateTimeField(default=now, blank=True)
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    valid = models.BooleanField(default=True)
    alert = models.BooleanField(default=False)
    
    def __str__(self):
        return self.auction.product + " - " + str(self.price) + " - " + self.user.username + " - " + str(self.date) + " - " + str(self.valid)

class Comment(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name='comments', null=True)
    name = models.CharField(max_length=80, blank=True)
    body = models.TextField(blank=True)
    created_on = models.DateTimeField(null=True,auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username + " - " + self.item.product


