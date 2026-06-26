from django.db import models

class Event(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('past', 'Past Event'),
    ]
    event_name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    event_date = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to='events/', blank=True, null=True)
    whatsapp_link = models.CharField(max_length=500, default='https://wa.me/918015913057')
    booking_link = models.CharField(max_length=500, blank=True, default='')
    event_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.event_name
