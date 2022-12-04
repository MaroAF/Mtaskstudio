from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CancelSubscriptionForm
from django.views.generic import FormView, View
from django.urls import reverse
from core.models import *
import sweetify
import stripe
from django.contrib.auth import get_user_model
User = get_user_model()

import stripe
from django.contrib import messages


class CancelSubscriptionView(LoginRequiredMixin, FormView):
    form_class=CancelSubscriptionForm

    def get_success_url(self):
        return reverse("user:profile", kwargs={"username": self.request.user.username})

    def form_valid(self, form):
        stripe.Subscription.delete(self.request.user.subscription.stripe_subsciption_id)
        stripe_customer_id = self.request.user.stripe_customer_id

        stripe_price_id = 'price_1M7lAGLkpd3BJqT8HbStIWI6'
        pricing = Pricing.objects.get(stripe_price_id = stripe_price_id)

        user = User.objects.get(stripe_customer_id=stripe_customer_id)
        user.subscription.status = 'active'
        user.subscription.stripe_subsciption_id ='sub_1M7nSsLkpd3BJqT8L4mOOqpx'
        user.subscription.pricing = pricing
        user.subscription.save()
        sweetify.success(self.request, "Suscripcion Cancelada con exito")
        return super().form_valid(form)


class UserSubscriptionView(View):
    def get(self, request, username,*args, **kwargs):
        if(request.user.is_authenticated):
            custumer_id = self.request.user.stripe_customer_id
            data = stripe.PaymentIntent.list(customer=custumer_id)
            iterate = len(data)
            suma = 0
            for e in range(iterate):
                number = data["data"][e]["amount"]
                suma = suma + number
            size = len(str(suma))            
            x = [int(a) for a in str(suma)]
            x.pop()
            x.pop()
            print(x)


            header = Header.objects.all()
            user = get_object_or_404(User, username=username)
            context={
                'user':user,
                'headers':header,
            }
            return render(request, 'users/user_profile.html',context)
        else:
            sweetify.error(self.request, "No has iniciado sesion")
            return redirect('account_login')

