#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.contrib.auth import authenticate, login, logout

from .forms import AdminLogin, AddCourses
from .models import Course, Student

def home(request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/admin/')
# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = AddCourses(request.POST)
		
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
#			if(form.cleaned_data['login_id']!='administrator'):
#				return render(request, 'hello_world/home.html')
#			if(form.cleaned_data['password']!='administrator'):
#				return render(request, 'hello_world/home.html')
            # ...
            # redirect to a new URL:
			return HttpResponseRedirect('/admin/courseadded/')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = AddCourses()

	course_list=Course.objects.all()
	student_list=Student.objects.all()
	return render(request, 'hello_world/home.html',{'course_list':course_list, 'student_list':student_list, 'form': form})
#	template=loader.get_template('hello_world/home.html')
#	return HttpResponse(template.render(request))
#def my_view(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)
#    if user is not None:
#        login(request, user)
        # Redirect to a success page.
#        ...
#    else:
        # Return an 'invalid login' error message.
#        ...
def login_page(request):
# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
                username=request.POST['login_id']
                password=request.POST['password']
		form = AdminLogin(request.POST)
		user = authenticate(username=username, password=password)
		
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
                        if user is not None:
                            login(request,user)
                            return HttpResponseRedirect('/admin/home/')
                        else:
                            form = AdminLogin()
                            return render(request, 'hello_world/login.html', {'form': form, 'error' : 'Invalid login id or password'})
#			if(form.cleaned_data['login_id']!='administrator'):
#				form = AdminLogin()
#				return render(request, 'hello_world/login.html', {'form': form, 'error' : 'Invalid login id'})
#			if(form.cleaned_data['password']!='administrator'):
#				form = AdminLogin()
#				return render(request, 'hello_world/login.html', {'form': form, 'error' : 'Invalid password'})
            # ...
            # redirect to a new URL:
			return HttpResponseRedirect('/admin/home/')

    # if a GET (or any other method) we'll create a blank form
	else:
		form = AdminLogin()

	return render(request, 'hello_world/login.html', {'form': form})

def course(request, code):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/admin/')
	this_course=Course.objects.get(course_code=code)
	students=this_course.enrolled_student.all()
	return render(request, 'hello_world/course.html', {'students': students})


#	template=loader.get_template('hello_world/login.html')
#	return HttpResponse(template.render(request))
# Create your views here.

def logout_page(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/admin/')
    logout(request)
    return render(request, 'hello_world/logout.html')

def courseadded(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/admin/')
    return render(request, 'hello_world/courseadded.html')
    