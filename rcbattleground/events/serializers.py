from rest_framework import serializers
from .models import Category, Event

# categoory serializer
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
    
 # event serializer
class EventSerializer(serializers.ModelSerializer): 
  class Meta:
    model = Event
    fields = '__all__'