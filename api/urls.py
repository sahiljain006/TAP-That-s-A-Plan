from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from events.models import Event
from gallery.models import GalleryImage
from contact.models import Contact

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def dashboard(request):
    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(event_status='upcoming').count()
    past_events = Event.objects.filter(event_status='past').count()
    total_gallery = GalleryImage.objects.count()
    total_enquiries = Contact.objects.count()
    return Response({
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'total_gallery': total_gallery,
        'total_enquiries': total_enquiries,
        'is_authenticated': request.user.is_authenticated,
        'is_staff': request.user.is_staff,
    })

urlpatterns = [
    path('events/', include('events.urls')),
    path('gallery/', include('gallery.urls')),
    path('contact/', include('contact.urls')),
    path('dashboard/', dashboard, name='dashboard'),
]
