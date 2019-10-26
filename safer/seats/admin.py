from django.contrib import admin
from .models import Event,Restaurant,Place


admin.site.register(Place)

admin.site.register(Event)

admin.site.register(Restaurant)
