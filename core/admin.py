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

@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title']
    search_fields = [
        'title'
    ]

@admin.register(ImagesAnimation)
class ImagesAnimationAdmin(admin.ModelAdmin):
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

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):    
    list_display = ['first_name']
    search_fields = [
        'first_name'
    ]

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title']
    search_fields = [
        'title'
    ]
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = [
        'title'
    ]

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name']
    search_fields = [
        'name'
    ]

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = [
        'user'
    ]