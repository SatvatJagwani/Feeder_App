#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth import authenticate, login, logout
import json
import csv
from .forms import AdminLogin, AddCourses, EnrollStudents
from .models import Course, Student

def home(request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/admin/')
        
        course_list=Course.objects.all()
        student_list=Student.objects.all()
# if this is a POST request we need to process the form data
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
                acform = AddCourses(request.POST)
                esform = EnrollStudents(request.POST)
        # check whether it's valid:
                if acform.is_valid():
                        (course, is_new)=Course.objects.get_or_create(name=acform.cleaned_data['course_name'],course_code=acform.cleaned_data['course_code'])
                    
                        if not is_new:
                                acform=AddCourses()
                                esform=EnrollStudents()
                                error='Course already exists'
                                return render(request, 'hello_world/home.html',{'course_list':course_list, 'student_list':student_list, 'add_course_form': acform, 'error_acform':error, 'enroll_student_form': esform})
                        course.feedbackform_set.create(name='midsem')
                        course.feedbackform_set.create(name='endsem')
                        for feedback_form in course.feedbackform_set.all():
                                feedback_form.question_set.create(question_text='Rating of the course as a whole:')
                                feedback_form.question_set.create(question_text='Rating of overall teaching of the instructor:')
                                feedback_form.question_set.create(question_text='Rating of the course content:')
                                feedback_form.question_set.create(question_text='Rating of problem discussion in the tutorial:')
                                for question in feedback_form.question_set.all():
                                    question.choice_set.create(choice_text='1 (Poor)')
                                    question.choice_set.create(choice_text='2 (Fair)')
                                    question.choice_set.create(choice_text='3 (Good)')
                                    question.choice_set.create(choice_text='4 (Very Good)')
                                    question.choice_set.create(choice_text='5 (Excellent)')
            # process the data in form.cleaned_data as required
#                        if(form.cleaned_data['login_id']!='administrator'):
#                                return render(request, 'hello_world/home.html')
#                        if(form.cleaned_data['password']!='administrator'):
#                                return render(request, 'hello_world/home.html')
            # ...
            # redirect to a new URL:
                        return HttpResponseRedirect('/admin/courseadded/')
                elif esform.is_valid():
                        course_set=Course.objects.filter(course_code=esform.cleaned_data['course_code'])
                        if not course_set.exists():
                                acform=AddCourses()
                                esform=EnrollStudents()
                                error='Course does not exist'
                                return render(request, 'hello_world/home.html',{'course_list':course_list, 'student_list':student_list, 'add_course_form': acform, 'error_esform':error, 'enroll_student_form': esform})
                        student_set=Student.objects.filter(roll_no=esform.cleaned_data['student_roll_no'])
                        if not student_set.exists():
                                acform=AddCourses()
                                esform=EnrollStudents()
                                error='Student is not enrolled'
                                return render(request, 'hello_world/home.html',{'course_list':course_list, 'student_list':student_list, 'add_course_form': acform, 'error_esform':error, 'enroll_student_form': esform})
                        for course in course_set:
                                for student in student_set:
                                        course.enrolled_student.add(student)
                        return HttpResponseRedirect('/admin/studentenrolled/')

    # if a GET (or any other method) we'll create a blank form
        else:
                acform = AddCourses()
                esform = EnrollStudents()

        return render(request, 'hello_world/home.html',{'course_list':course_list, 'student_list':student_list, 'add_course_form': acform, 'enroll_student_form': esform})
#        template=loader.get_template('hello_world/home.html')
#        return HttpResponse(template.render(request))
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
                with open('hello_world/templates/hello_world/registered_students.csv') as f:
                    reader = list(csv.reader(f))
                    for row in reader[1:]:
                        Student.objects.get_or_create(name=row[0],roll_no=row[1],password=row[2],)
            # creates a tuple of the new object or
            # current object and a boolean of if it was created
        # check whether it's valid:
                if form.is_valid():
            # process the data in form.cleaned_data as required
                        if user is not None:
                            login(request,user)
                            
                            return HttpResponseRedirect('/admin/home/')
                        else:
                            form = AdminLogin()
                            return render(request, 'hello_world/login.html', {'form': form, 'error' : 'Invalid login id or password'})
#                        if(form.cleaned_data['login_id']!='administrator'):
#                                form = AdminLogin()
#                                return render(request, 'hello_world/login.html', {'form': form, 'error' : 'Invalid login id'})
#                        if(form.cleaned_data['password']!='administrator'):
#                                form = AdminLogin()
#                                return render(request, 'hello_world/login.html', {'form': form, 'error' : 'Invalid password'})
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


#        template=loader.get_template('hello_world/login.html')
#        return HttpResponse(template.render(request))
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

def studentenrolled(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/admin/')
    return render(request, 'hello_world/studentenrolled.html')

def login_app(request):
# if this is a POST request we need to process the form data
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
                json_data=json.loads(request.body)
                username=json_data['login_name']
                password=json_data['password']
                student_set=Student.objects.filter(name=username)
                if not student_set.exists():
                    return JsonResponse({'response':"Invalid user"})
                student_set=Student.objects.filter(password=password)
                if not student_set.exists():
                    return JsonResponse({'response':"Invalid password"})
                return JsonResponse({'response':"yes"})
        else:
                return HttpResponse('get')
