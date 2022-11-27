from django import forms
from .models import ServiceProviders,Services,Comment
from dataclasses import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model=ServiceProviders
        fields='__all__'


# class ServiceQueryForm(forms.ModelForm):
#     class Meta:
#         model= Queries
#         fields='__all__'


# class ServiceAnswer(forms.ModelForm):
#     class Meta:
#         model=QueryAnswer
 #        fields='__all__'


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model=Comment
#         fields=('Comment','User','Service_provider')
#         widgets={
            
#             'Comment':forms.Textarea(attrs={'class':'form-control'}),
#         }

class AddServiceForm(forms.ModelForm):
    class Meta:
        service = forms.CharField(label = 'service', required = False)
        model=ServiceProviders
        fields=('Category',)