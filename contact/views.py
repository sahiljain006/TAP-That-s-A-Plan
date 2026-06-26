from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            'success': True,
            'message': 'Thank you for reaching out! We will get back to you soon.'
        }, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)
