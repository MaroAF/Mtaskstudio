from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from core.models import *

# Create your views here.

def index(request):
    header = Header.objects.all()
    banner = Schedule.objects.all()
    context = {
        'headers':header,
        'banners':banner,
    }
    return render(request, 'index.html', context)


def schedule(request):
    header = Header.objects.all()
    schedule = Schedule.objects.all()
    context = {
        'headers':header,
        'schedules':schedule,
    }
    return render(request, 'schedule.html',context)

def sets(request,slug):    
    header = Header.objects.all()
    schedule = get_object_or_404(Schedule, slug = slug)
    place = get_object_or_404(Placeholder)
    context = {
        'headers':header,
        'schedule':schedule,
        'place':place,
    }
    return render(request, 'view-sets.html',context)

def page_not_found(request, exception):
    return render(request, 'error/404.html', status=404)