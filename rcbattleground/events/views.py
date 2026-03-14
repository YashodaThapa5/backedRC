from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import filters
from .filters import EventFilter

# getting all categories 
class CategoryListView(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [AllowAny] #anyone can view categories
  
# adding new category
class CategoryCreateView(generics.CreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAdminUser] #only admin can add category
  
# retrieving  category
class CategoryRetrieveView(generics.RetrieveUpdateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [AllowAny] #anyone can view categories
  
# updating  category
class CategoryUpdateView(generics.UpdateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAdminUser] #only admin can update category

# deleting category
class CategoryDeleteView(generics.DestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAdminUser] #only admin can delete category 


# getting and adding new events
class EventCreateListView(generics.ListCreateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  
  filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
  # filterset_fields = ['category'] # http://127.0.0.1:8000/api/events/?category=id
  
  filterset_class = EventFilter #custom filter for 
  
  search_fields = ['name', 'description', 'category__name'] # http://http://127.0.0.1:8000/api/events/?search=keyword
  
  # http://127.0.0.1:8000/api/events/?ordering=created_at or -created_at or -price or price or event_date or -event_date
  ordering_fields = ['created_at', 'event_date', 'price'] # http://
  

# retrieving, updating, and deleting a specific event
class EventRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  