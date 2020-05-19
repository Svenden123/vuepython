from django.contrib import admin

# Register your models here.
from api_v1.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'created_at']
