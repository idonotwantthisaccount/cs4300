from django.db import models

# Create your models here.

class Movie(models.Model):
    title_text = models.CharField(max_length=50)
    Description_text = models.CharField(max_length=500)
    release_date = models.DateTimeField("release date")

class seat(models.Model):
    seat_number = models.IntegerField(default=0)
    booking_status = models.BooleanField.()

class booking(models.Model):
    movie = models.CharField(max_length=50)
    seat = models.IntegerField(default=0)
    user = models.CharField(max_length=50)
    booking_date = models.DateTimeField("current date")