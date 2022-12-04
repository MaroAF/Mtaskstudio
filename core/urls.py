import imp
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name="home"),
    path('agendar',views.schedule,name="schedule"), 
    path('agendar/sets/<slug:slug>/',views.sets,name="set"),
    path('nuestros-trabajos',views.works,name="works"), 
    path('cursos',views.courses,name="courses"), 
    path('cursos/<slug:slug>/',views.courses_view,name="course_view"),
    path('prices/',views.pricesView,name="prices"), 
    path('payment/<slug:slug>',views.paymentsView,name="payment"),
    path('payment/create-subscription/', views.CreateSubscriptionView.as_view(), name='create-subscription'),
    path('payment/thank-you/',views.ThankYouView,name="thank-you"), 
    path('payment/retry-invoice/', views.RetryInvoiceView.as_view(), name='retry-invoice'),
    path('change-subscription/', views.ChangeSubscriptionView.as_view(), name='change-subscription'),
    path('payment/webhook/', views.webhook, name='webhook'),

    path('cursos/<slug:slug>/<int:chapter_number>/', views.get_data_ajax, name='ajax')
]