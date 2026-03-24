
from django.urls import path

from .views import *

urlpatterns = [
    # http://127.0.0.1:8000/api/categories/ 
    path('categories/', CategoryListView.as_view(), name='category-list'),
    
    # http://127.0.0.1:8000/api/categories/add/
    path('categories/add/', CategoryCreateView.as_view(), name='add-category'),
    
    # http://127.0.0.1:8000/api/categories/1
    path('categories/<int:pk>', CategoryRetrieveView.as_view(), name='single-category'),
    
    # http://127.0.0.1:8000/api/categories/update/1
    path('categories/update/<int:pk>', CategoryUpdateView.as_view(), name='update-category'),
    
    # http://127.0.0.1:8000/api/categories/delete/1
    path('categories/delete/<int:pk>', CategoryDeleteView.as_view(), name='delete-category'),
    
    
    # get and add events api
    # http://127.0.0.1:8000/api/events/
    path('events/', EventCreateListView.as_view(), name='event-list-create'),
    
    # get, update, and delete a specific event
    # http://127.0.0.1:8000/api/events/1/
    path('events/<int:pk>/', EventRetrieveUpdateDeleteView.as_view(), name='event-retrieve-update-delete'),

    # Slots
    path('slots/', SlotListCreateView.as_view(), name='slot-list-create'),
    path('slots/<int:pk>/', SlotRetrieveUpdateDeleteView.as_view(), name='slot-retrieve-update-delete'),

    # Bookings
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDeleteView.as_view(), name='booking-retrieve-update-delete'),
    
    # User's bookings
    # http://127.0.0.1:8000/api/bookings/my/
    path('bookings/my/', UserBookingListView.as_view(), name='my-bookings'),
    
    path("slot-bookings/", SlotBookingCreateView.as_view(), name="slot-bookings"),
    
  
]
