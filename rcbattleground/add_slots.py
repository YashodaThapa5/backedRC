#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rcbattleground.settings')
sys.path.append('/Users/shyammagar/Documents/Backend (RC Battleground)/rcbattleground')
django.setup()

from events.models import Slot

# Create sample slots
slots_data = [
    {
        'slotTitle': 'Morning Yoga Session',
        'description': 'Start your day with energizing yoga',
        'price': 25.00,
        'maximumseats': 10,
        'times': ['8:00 AM', '9:00 AM', '10:00 AM']
    },
    {
        'slotTitle': 'Afternoon Workout',
        'description': 'High-intensity training session',
        'price': 35.00,
        'maximumseats': 8,
        'times': ['2:00 PM', '3:00 PM', '4:00 PM']
    },
    {
        'slotTitle': 'Evening Meditation',
        'description': 'Relax and unwind with guided meditation',
        'price': 20.00,
        'maximumseats': 15,
        'times': ['6:00 PM', '7:00 PM', '8:00 PM']
    }
]

for slot_data in slots_data:
    slot, created = Slot.objects.get_or_create(
        slotTitle=slot_data['slotTitle'],
        defaults=slot_data
    )
    if created:
        print(f"Created slot: {slot.slotTitle}")
    else:
        print(f"Slot already exists: {slot.slotTitle}")

print("Sample slots creation completed!")