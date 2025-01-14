from django.contrib import admin
from .models import Flat, Complaint, Owner


class AdminInline(admin.TabularInline):
    model = Owner.flats_in_ownership.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'construction_year']
    exclude = ('flats_in_ownership',)
    inlines = [
        AdminInline
    ]
    
    
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'author',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats_in_ownership',)
