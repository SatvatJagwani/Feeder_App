from django import forms

class InstructorLogin(forms.Form):
	name = forms.CharField(label='Name', max_length=100)
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())

class InstructorSignup(forms.Form):
	name = forms.CharField(label='Name', max_length=100)
	email_id = forms.CharField(label='Email id', max_length=100, widget=forms.EmailInput())
	password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())

class AddCourseFeedback(forms.Form):
    course_code = forms.CharField(label='Course Code', max_length=100)
    name = forms.CharField(label='Feedback name', max_length=100)
    deadline = forms.DateTimeField(label='Feedback deadline (MM/DD/YYYY HH:MM)', widget=forms.DateTimeInput(format='%m/%d/%Y %H:%M:%S.%f'))
    question_1=forms.CharField(label='Question #1', max_length=100)
    question_2=forms.CharField(label='Question #2', max_length=100)
    question_3=forms.CharField(label='Question #3', max_length=100)
    question_4=forms.CharField(label='Question #4', max_length=100)
    

class EnrollStudents(forms.Form):
    course_code = forms.CharField(label='Course Code', max_length=100)
    student_roll_no = forms.CharField(label='Student Roll No', max_length=100)