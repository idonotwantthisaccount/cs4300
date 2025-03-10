from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, book_seat, booking_history

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    
    # Template-based views
    path('', movie_list, name='movie_list'),
    path('book/<int:movie_id>/', book_seat, name='book_seat'),
    path('history/', booking_history, name='booking_history'),
]
