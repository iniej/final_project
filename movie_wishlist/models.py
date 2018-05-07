from django.db import models

# Create your models here.


# Create a model for the user information, making the use email address
# and user name unique.
class UserInfo(models.Model):
    username = models.CharField(max_length = 40, unique = True, blank = False)
    firstname = models.CharField(max_length = 200, blank = False)
    lastname = models.CharField(max_length = 200, blank = False)
    email = models.CharField(max_length = 200, unique = True,blank = False)
    password1 = models.CharField(max_length = 200, blank = False)
    password2 = models.CharField(max_length = 200, blank = False)

# Create a movie watchlist model
class WatchList(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    actor = models.CharField(max_length=200)
    director = models.CharField(max_length=200)


# Create a movie watchedlist model
class WatchedList(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    actor = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    rating = models.CharField(max_length = 2, blank=True)
