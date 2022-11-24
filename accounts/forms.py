from django import forms
from allauth.account.forms import SignupForm,LoginForm
from django.contrib import messages
from allauth.account.adapter import DefaultAccountAdapter
import sweetify



class CancelSubscriptionForm(forms.Form):
    hidden = forms.HiddenInput()

class CustomSignupForm(SignupForm):
    full_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Nombre completo'}))
    perfil_photo = forms.ImageField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["full_name"].label = "Nombre Completo"
        self.fields["perfil_photo"].label = "Foto de perfil"

    def save(self, request):

        
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        
        user.full_name = self.cleaned_data['full_name']
        user.perfil_photo = self.cleaned_data['perfil_photo']
             
        user.save()

        # You must return the original result.
        return user
