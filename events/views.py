from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        qs = Event.objects.all()
        status = self.request.query_params.get('status')
        if status:
            qs = qs.filter(event_status=status)
        return qs

    @action(detail=False, methods=['get'])
    def stats(self, request):
        total = Event.objects.count()
        upcoming = Event.objects.filter(event_status='upcoming').count()
        past = Event.objects.filter(event_status='past').count()
        return Response({
            'total_events': total,
            'upcoming_events': upcoming,
            'past_events': past,
        })
