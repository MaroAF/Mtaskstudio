import imp
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name="home"),
    path('agendar',views.schedule,name="schedule"), 
    path('agendar/sets/<slug:slug>/',views.sets,name="set"),   
]