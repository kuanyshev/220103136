from django.db import models

class Item(models.Model):
    STATUS_CHOICES = [
        ('unclaimed', 'Unclaimed'),
        ('claimed', 'Claimed'),
        ('auction', 'Auction'),
    ]

    name = models.CharField(max_length=200) 
    category = models.CharField(max_length=100) 
    location = models.CharField(max_length=100) 
    date_found = models.DateField(date_found = models.DateField()) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unclaimed')

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"
