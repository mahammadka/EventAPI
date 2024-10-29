from django.contrib import admin
from .models import Event

# Register the Event model with the Django admin site
admin.site.register(Event)