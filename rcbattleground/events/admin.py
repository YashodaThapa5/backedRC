from django.contrib import admin
from .models import Category, Event, Slot, Booking

# Register your models here.
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Slot)
admin.site.register(Booking)