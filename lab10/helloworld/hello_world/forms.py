from django import forms

class AdminLogin(forms.Form):
	login_id = forms.CharField(label='Login id', max_length=100)
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())

class AddCourses(forms.Form):
    course_name = forms.CharField(label='Course Name', max_length=100)
    course_code = forms.CharField(label='Course Code', max_length=100)

class EnrollStudents(forms.Form):
    course_code = forms.CharField(label='Course Code', max_length=100)
    student_roll_no = forms.CharField(label='Student Roll No', max_length=100)