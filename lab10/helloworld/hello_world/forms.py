from django import forms

class AdminLogin(forms.Form):
	login_id = forms.CharField(label='Login id', max_length=100)
	password = forms.CharField(label='Password', max_length=100)