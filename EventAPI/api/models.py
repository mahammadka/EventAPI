from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model that extends AbstractUser
class User(AbstractUser):
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('user', 'User')], default='user')

# Event model to represent an event
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    total_tickets = models.IntegerField()
    tickets_sold = models.IntegerField(default=0)

# Ticket model to represent a ticket purchased by a user for an event
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateField(auto_now_add=True)
