# -*- encoding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
	Email	= forms.EmailField(widget=forms.TextInput())
	Titulo	= forms.CharField(widget=forms.TextInput())
	Texto	= forms.CharField(widget=forms.Textarea())


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search'}) ,label='Usuario' )
	password = forms.CharField(widget=forms.PasswordInput(render_value=False) ,label='Contraseña' )
	


