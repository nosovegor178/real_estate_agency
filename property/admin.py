from django.contrib import admin
from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'construction_year']

admin.site.register(Flat, FlatAdmin)
