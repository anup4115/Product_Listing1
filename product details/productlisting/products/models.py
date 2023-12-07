from django.db import models

# Create your models here.
class Products(models.Model):
    AVAILABLE = 'available'
    NOT_AVAILABLE = 'not_available'
    
    AVAILABILITY_CHOICES = [
        (AVAILABLE, 'Available'),
        (NOT_AVAILABLE, 'Not Available'),
    ]
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField()
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default=AVAILABLE,
    )
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    
from django.db import models

class ContactMessage(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.created_at}"