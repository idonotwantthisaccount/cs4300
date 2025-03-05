from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from datetime import datetime
from .models import Movie, Seat, Booking

class MovieAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title_text="Test Movie",
            description_text="A test movie description.",
            release_date=datetime(2020, 1, 1)
        )

    def test_list_movies(self):
        # Assuming your router registers the MovieViewSet with basename 'movie'
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Movie", str(response.data))
    
    def test_create_movie(self):
        url = reverse('movie-list')
        data = {
            "title_text": "New Movie",
            "description_text": "This is a newly created movie.",
            "release_date": "2023-01-01T00:00:00Z"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verify that a new movie has been added
        self.assertEqual(Movie.objects.count(), 2)

class BookingAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a movie and a seat for the booking test
        self.movie = Movie.objects.create(
            title_text="Booking Movie",
            description_text="For booking testing.",
            release_date=datetime(2021, 1, 1)
        )
        self.seat = Seat.objects.create(
            seat_number=1,
            booking_status=False
        )

    def test_create_booking(self):
        # Assuming your router registers the BookingViewSet with basename 'booking'
        url = reverse('booking-list')
        data = {
            "movie": self.movie.title_text,  # if you're storing movie title
            "seat": self.seat.seat_number,     # if storing seat number
            "user": "Test User"
            # booking_date should auto-populate if using auto_now_add=True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Refresh seat from db and check its status is updated to booked
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.booking_status)
