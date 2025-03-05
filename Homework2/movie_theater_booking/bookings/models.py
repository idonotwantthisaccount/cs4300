from django.db import models

class Movie(models.Model):
    title_text = models.CharField(max_length=50)
    description_text = models.CharField(max_length=500)  
    release_date = models.DateTimeField("release date")
    
    def __str__(self):
        return self.title_text

class Seat(models.Model):
    seat_number = models.IntegerField(default=0)
    booking_status = models.BooleanField(default=False)  

    def __str__(self):
        status = "Booked" if self.booking_status else "Available"
        return f"Seat {self.seat_number} ({status})"

class Booking(models.Model):
    movie = models.CharField(max_length=50)
    seat = models.IntegerField(default=0)
    user = models.CharField(max_length=50)
    booking_date = models.DateTimeField("current date", auto_now_add=True)

    def __str__(self):
        return f"{self.user} booked seat {self.seat} for {self.movie}"

