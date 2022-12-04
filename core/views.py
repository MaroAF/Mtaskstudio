from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import Paginator
from core.models import *
from django.conf import settings
from rest_framework.views import APIView
import sweetify
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth import get_user_model
from allauth.account.views import LogoutView
User = get_user_model()

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
from django.contrib import messages

# Create your views here.
 
def index(request):
    header = Header.objects.all()
    banner = Schedule.objects.all()
    price = Pricing.objects.all().order_by('id')
    imagesA = ImagesAnimation.objects.all()
    context = {
        'headers':header,
        'banners':banner,
        'images':imagesA,
        'prices':price,
    }
    return render(request, 'index.html', context)

# messages
def login_succes(sender, user, request, **kwargs):
    sweetify.success(request, f"Bienvenido {user}")

user_logged_in.connect(login_succes)

#sets
def schedule(request):
    header = Header.objects.all()
    schedule = Schedule.objects.all()
    context = {
        'headers':header,
        'schedules':schedule,
    }
    return render(request, 'Schedule/schedule.html',context)

def sets(request,slug):    
    header = Header.objects.all()
    schedule = get_object_or_404(Schedule, slug = slug)
    place = get_object_or_404(Placeholder)
    context = {
        'headers':header,
        'schedule':schedule,
        'place':place,
    }
    return render(request, 'Schedule/view-sets.html',context)

def works(request):
    header = Header.objects.all()
    works = Works.objects.all()
    context = {
        'headers':header,
        'works':works,
    }
    return render(request, 'works/works.html',context)
#CURSOS
def courses(request):
    header = Header.objects.all()  
    courses = Courses.objects.filter(active=True)  
    
    context = {
        'headers':header,
        'courses':courses
    }
    return render(request, 'courses/courses.html',context)

def courses_view(request,slug):    
    header = Header.objects.all()
    course_view = get_object_or_404(Courses, slug = slug) 
    chapter = Chapter.objects.filter(course__slug = slug)
    context = {
        'headers':header,
        'data':course_view,
        'chapters': chapter,
    }
    if(request.user.is_authenticated):
        subscription = request.user.subscription
        pricin_tier = subscription.pricing
        subscription_is_active = subscription.status == "active" or subscription.status == "trialing"
        print(subscription_is_active)
        context.update({
            "has_permission": pricin_tier in course_view.pricing_tier.all() and subscription_is_active
        })
    return render(request, 'courses/courses_view.html',context)

def get_data_ajax(request, slug,chapter_number):
    course_view = get_object_or_404(Courses, slug = slug)    
    subscription = request.user.subscription
    pricin_tier = subscription.pricing
    subscription_is_active = subscription.status == "active" or subscription.status == "trialing"
    chapter = list(Chapter.objects.filter(course__slug = slug).filter(chapter_number = chapter_number).values())
    course = list(Courses.objects.filter(slug = slug).values())
    status = pricin_tier in course_view.pricing_tier.all() and subscription_is_active
    message = str(subscription) +"-"+ str(subscription_is_active)
    if(status==True):
        if (len(chapter)>0):
            data = {'message': message, 'chapters': chapter,'course': course}
        else:
            data = {'message': "Not found"}
    else:
        data = {'message': "No-permitido"}


    return JsonResponse(data)

#PAYMENTS

@csrf_exempt
def webhook(request):
    # You can use webhooks to receive information about asynchronous payment events.
    # For more about our webhook events check out https://stripe.com/docs/webhooks.
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET
    payload = request.body

    # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
    signature = request.META["HTTP_STRIPE_SIGNATURE"]
    try:
        event = stripe.Webhook.construct_event(
            payload=payload, sig_header=signature, secret=webhook_secret)
        data = event['data']
    except Exception as e:
        return e
    # Get the type of webhook event sent - used to check the status of PaymentIntents.
    event_type = event['type']
    data_object = data['object']
    if event_type == 'payment_intent.succeeded':
        print(data_object)
        
    if event_type == 'invoice.paid':
        webhook_object = data["object"]
        stripe_customer_id = webhook_object["customer"]

        stripe_sub = stripe.Subscription.retrieve(webhook_object["subscription"])
        stripe_price_id = stripe_sub["plan"]["id"]

        pricing = Pricing.objects.get(stripe_price_id = stripe_price_id)

        user = User.objects.get(stripe_customer_id=stripe_customer_id)
        user.subscription.status = stripe_sub["status"]
        user.subscription.stripe_subsciption_id = webhook_object["subscription"]
        user.subscription.pricing = pricing
        user.subscription.save()
        

    if event_type == 'invoice.payment_failed':
        # If the payment fails or the customer does not have a valid payment method,
        # an invoice.payment_failed event is sent, the subscription becomes past_due.
        # Use this webhook to notify your user that their payment has
        # failed and to retrieve new card details.
        print(data)

    if event_type == 'customer.subscription.deleted':
        webhook_object = data["object"]
        stripe_customer_id = webhook_object["customer"]
        stripe_sub = stripe.Subscription.retrieve(webhook_object["id"])
        user = User.objects.get(stripe_customer_id=stripe_customer_id)
        user.subscription.status = stripe_sub["status"]
        user.subscription.save()

    return HttpResponse()



def pricesView(request):
    header = Header.objects.all()
    price = Pricing.objects.all()
    context = {
        'headers':header,
        'prices':price
    }
    
    return render(request, 'payments/pricing.html',context)

def ThankYouView(request):
    header = Header.objects.all()
    banner = Schedule.objects.all()
    context = {
        'headers':header,
        'banners':banner,
    }
    sweetify.success(request, "Su compra fue realizada con exito", timer=3000)
    return render(request, 'index.html', context)

def paymentsView(request, slug):
    header = Header.objects.all()
    pricing = get_object_or_404(Pricing, slug = slug)
    subscription = request.user.subscription

    if subscription.pricing == pricing and subscription.is_active:
        messages.info(request, "Ya tienes esta suscripcion")
        return redirect("prices")

    context = {
        'headers':header,
        'prices':pricing,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    }  
    if subscription.is_active and subscription.pricing.stripe_price_id != "price_1M7lAGLkpd3BJqT8HbStIWI6":
            return render(request, "payments/change.html", context)  

    return render(request, 'payments/checkout.html',context)

def paymentsViewUnique(request, slug):
    header = Header.objects.all()
    schedule = get_object_or_404(Schedule, slug = slug)

    context = {
        'headers':header,
        'schedule':schedule,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    }  
    return render(request, 'payments/checkout.html',context)


class CreateSubscriptionView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        customer_id = request.user.stripe_customer_id
        
        try:
            #vincular el metodo de pago al cliente
            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=customer_id
            )

            #configuurar metodod e apgo prederterminado del cliente
            stripe.Customer.modify(
                customer_id,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            #crear suscripcion
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{'price': data["priceId"]}],
                expand=['latest_invoice.payment_intent'],
            )

            data = {}
            data.update(subscription)

            return Response(data)
        except Exception as e:
            return Response({
                "error": {'message': str(e)}
            })

class RetryInvoiceView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        customer_id = request.user.stripe_customer_id
        try:

            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=customer_id,
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                customer_id,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            invoice = stripe.Invoice.retrieve(
                data['invoiceId'],
                expand=['payment_intent'],
            )
            data = {}
            data.update(invoice)

            return Response(data)
        except Exception as e:

            return Response({
                "error": {'message': str(e)}
            })

class ChangeSubscriptionView(APIView):
    def post(self, request, *args, **kwargs):

        subscription_id = request.user.subscription.stripe_subsciption_id
        subscription = stripe.Subscription.retrieve(subscription_id)
        try:
            updatedSubscription = stripe.Subscription.modify(
                subscription_id,
                cancel_at_period_end=False,
                items=[{
                    'id': subscription['items']['data'][0].id,
                    'price': request.data["priceId"],
                }],
                proration_behavior="always_invoice"
            )

            data = {}
            data.update(updatedSubscription)
            return Response(data)
        except Exception as e:
            return Response({
                "error": {'message': str(e)}
            })

#PAGINA NO ENCONTRADA
def page_not_found(request, exception):
    return render(request, 'error/404.html', status=404)