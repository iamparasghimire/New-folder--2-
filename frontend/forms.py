from django import forms
from .models import Contact, Enroll
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    pass 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = ['name', 'email', 'phone', 'education', 'attempts','desired_score']

        
        