from django.db import models
from django.contrib.auth.models import User
from tables.models import Table

class Reservation(models.Model):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELED = 'canceled'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELED, 'Canceled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    table = models.ForeignKey(Table, on_delete=models.CASCADE) 
    date = models.DateField() 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)  # Статус брони

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.date}"
