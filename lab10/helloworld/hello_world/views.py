#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .forms import AdminLogin
from .models import Course, Student

def home(request):
	course_list=Course.objects.all()
	student_list=Student.objects.all()
	return render(request, 'hello_world/home.html',{'course_list':course_list, 'student_list':student_list})
#	template=loader.get_template('hello_world/home.html')
#	return HttpResponse(template.render(request))

def login(request):
# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = AdminLogin(request.POST)
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
			if(form.cleaned_data['login_id']!='administrator'):
				form = AdminLogin()
				return render(request, 'hello_world/login.html', {'form': form, 'error' : 'Invalid login id'})
			if(form.cleaned_data['password']!='administrator'):
				form = AdminLogin()
				return render(request, 'hello_world/login.html', {'form': form, 'error' : 'Invalid password'})
            # ...
            # redirect to a new URL:
			return HttpResponseRedirect('/admin/home/')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = AdminLogin()

	return render(request, 'hello_world/login.html', {'form': form})

def course(request, code):
	this_course=Course.objects.get(course_code=code)
	students=this_course.enrolled_student.all()
	return render(request, 'hello_world/course.html', {'students': students})


#	template=loader.get_template('hello_world/login.html')
#	return HttpResponse(template.render(request))
# Create your views here.
