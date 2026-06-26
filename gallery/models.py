from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=255, blank=True, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title or f"Gallery Image #{self.id}"
