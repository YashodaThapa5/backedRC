import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    start_date = django_filters.DateFilter(field_name='event_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='event_date', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['category', 'min_price', 'max_price', 'start_date', 'end_date']
