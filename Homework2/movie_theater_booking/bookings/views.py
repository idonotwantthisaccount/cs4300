from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Define API viewsets for CRUD operations

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Optional: If you have template-based views, define them below

from django.shortcuts import render, get_object_or_404, redirect

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(booking_status=False)
    if request.method == "POST":
        seat_id = request.POST.get('seat')
        user = request.POST.get('user')
        seat = get_object_or_404(Seat, id=seat_id)
        seat.booking_status = True
        seat.save()
        Booking.objects.create(movie=movie.title_text, seat=seat.seat_number, user=user)
        return redirect('booking_history')
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
