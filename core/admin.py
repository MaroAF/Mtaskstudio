from django.contrib import admin
from core.models import *

# Register your models here.
@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = [
        'title',
    ]

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title']
    search_fields = [
        'title'
    ]

@admin.register(Placeholder)
class PlaceHolderAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = [
        'title'
    ]

