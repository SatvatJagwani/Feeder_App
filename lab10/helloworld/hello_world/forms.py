from django import forms

class AdminLogin(forms.Form):
	login_id = forms.CharField(label='Login id', max_length=100)
	password = forms.CharField(label='Password', max_length=100)

class AddCourses(forms.Form):
    course_name = forms.CharField(label='Course Name', max_length=100)
    course_code = forms.CharField(label='Course Code', max_length=100)