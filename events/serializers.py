from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'event_name', 'venue', 'description', 'event_date',
                  'event_image', 'image_url', 'whatsapp_link', 'booking_link',
                  'event_status', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_image_url(self, obj):
        if obj.event_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.event_image.url)
            return obj.event_image.url
        return None
