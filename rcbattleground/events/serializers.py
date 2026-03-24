from rest_framework import serializers
from .models import Category, Event, Slot, Booking


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    event_name = serializers.CharField(source='event.name', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'user',
            'event',
            'event_name',
            'booking_date',
            'booking_time',
            'status',
            'created_at'
        ]
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        event = data['event']
        booking_date = data['booking_date']
        booking_time = data['booking_time']

        existing_bookings = Booking.objects.filter(
            event=event,
            booking_date=booking_date,
            booking_time=booking_time
        ).count()

        if existing_bookings >= event.event_seats:
            raise serializers.ValidationError("No seats available for this time.")
        

        return data