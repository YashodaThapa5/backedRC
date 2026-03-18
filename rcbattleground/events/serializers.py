from rest_framework import serializers
from .models import Category, Event, Slot, Booking

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

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # To show username
    event_name = serializers.CharField(source='event.name', read_only=True)  # To show event name

    class Meta:
        model = Booking
        fields = ['id', 'user', 'event', 'event_name', 'booking_date', 'booking_time', 'status', 'created_at']

    def validate(self, data):
        event = data['event']
        booking_date = data['booking_date']
        booking_time = data['booking_time']

        # Check if the time is available for the event
        if booking_time not in event.times:
            raise serializers.ValidationError("Invalid time for this event.")

        # Check if seats are available
        existing_bookings = Booking.objects.filter(
            event=event,
            booking_date=booking_date,
            booking_time=booking_time
        ).count()

        if existing_bookings >= event.event_seats:
            raise serializers.ValidationError("No seats available for this time.")

        return data        

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # To show username
    slot_title = serializers.CharField(source='slot.slotTitle', read_only=True)  # To show slot title

    class Meta:
        model = Booking
        fields = ['id', 'user', 'slot', 'slot_title', 'booking_date', 'booking_time', 'status', 'created_at']

    def validate(self, data):
        slot = data['slot']
        booking_date = data['booking_date']
        booking_time = data['booking_time']

        # Check if the time is available for the slot
        if booking_time not in slot.times:
            raise serializers.ValidationError("Invalid time for this slot.")

        # Check if seats are available
        existing_bookings = Booking.objects.filter(
            slot=slot,
            booking_date=booking_date,
            booking_time=booking_time
        ).count()

        if existing_bookings >= slot.maximumseats:
            raise serializers.ValidationError("No seats available for this time slot.")

        return data