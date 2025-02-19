from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'date_found', 'status')
    list_filter = ('status', 'category', 'location')
    search_fields = ('name', 'category', 'location')

