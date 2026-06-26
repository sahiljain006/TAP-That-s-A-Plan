from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'venue', 'event_date', 'event_status', 'created_at']
    list_filter = ['event_status']
    search_fields = ['event_name', 'venue']
