from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InstructorLogin, InstructorSignup, AddCourseFeedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from hello_world.models import AdminOrInstructor, Course, FeedbackForm, Question, Choice
# Create your views here.
def login_page(request):

# if this is a POST request we need to process the form data
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
                loginform = InstructorLogin(request.POST)
                signupform = InstructorSignup(request.POST)
        # check whether it's valid:
                if signupform.is_valid():
                        #(course, is_new)=Course.objects.get_or_create(name=acform.cleaned_data['course_name'],course_code=acform.cleaned_data['course_code'])
                    
                        #if not is_new:
                                #acform=AddCourses()
                                #esform=EnrollStudents()
                                #error='Course already exists'
                                #return render(request, 'hello_world/home.html',{'course_list':course_list, 'student_list':student_list, 'add_course_form': acform, 'error_acform':error, 'enroll_student_form': esform})
                        name = signupform.cleaned_data['name']
                        email_id = signupform.cleaned_data['email_id']
                        password = signupform.cleaned_data['password']
                        user = User.objects.create_user(name, email_id, password)
                        AdminOrInstructor.objects.create(user=user)
                        #course.feedbackform_set.create(name='midsem')
                        #course.feedbackform_set.create(name='endsem')
                        #for feedback_form in course.feedbackform_set.all():
                                #feedback_form.question_set.create(question_text='Rating of the course as a whole:')
                                #feedback_form.question_set.create(question_text='Rating of overall teaching of the instructor:')
                                #feedback_form.question_set.create(question_text='Rating of the course content:')
                                #feedback_form.question_set.create(question_text='Rating of problem discussion in the tutorial:')
                                #for question in feedback_form.question_set.all():
                                    #question.choice_set.create(choice_text='1 (Poor)')
                                    #question.choice_set.create(choice_text='2 (Fair)')
                                    #question.choice_set.create(choice_text='3 (Good)')
                                    #question.choice_set.create(choice_text='4 (Very Good)')
                                    #question.choice_set.create(choice_text='5 (Excellent)')
            # process the data in form.cleaned_data as required
#                        if(form.cleaned_data['login_id']!='administrator'):
#                                return render(request, 'hello_world/home.html')
#                        if(form.cleaned_data['password']!='administrator'):
#                                return render(request, 'hello_world/home.html')
            # ...
            # redirect to a new URL:
                        return HttpResponseRedirect('/instructor/instructoradded/')
                elif loginform.is_valid():
                        user = authenticate(username=loginform.cleaned_data['name'],password=loginform.cleaned_data['password'])
                        if user is not None and user.adminorinstructor.type == 'instructor':
                                login(request,user)
                                return HttpResponseRedirect('/instructor/home/')
                        else:
                                loginform = InstructorLogin()
                                signupform = InstructorSignup()
                                return render(request, 'instructor/login.html',{'login_form':loginform, 'signup_form':signupform, 'error':'invalid email id or password'})
    # if a GET (or any other method) we'll create a blank form
        else:
                loginform = InstructorLogin()
                signupform = InstructorSignup()

        return render(request, 'instructor/login.html',{'login_form':loginform, 'signup_form':signupform})

def home(request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/instructor/')
        
        #course_list=Course.objects.all()
        #student_list=Student.objects.all()
# if this is a POST request we need to process the form data
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
                fbform = AddCourseFeedback(request.POST)
                #esform = EnrollStudents(request.POST)
        # check whether it's valid:
                if fbform.is_valid():
                        course_set=Course.objects.filter(course_code=fbform.cleaned_data['course_code'])
                        #(course, is_new)=Course.objects.get_or_create(name=acform.cleaned_data['course_name'],course_code=acform.cleaned_data['course_code'])
                    
                        if not course_set.exists():
                                fbform=AddCourseFeedback()
                                #esform=EnrollStudents()
                                error='Course does not exist'
                                return render(request, 'instructor/home.html',{'feedback_form':fbform,  'error':error})
                        for course in course_set:
                                feedback_form=course.feedbackform_set.create(name=fbform.cleaned_data['name'])
                                feedback_form.deadline=fbform.cleaned_data['deadline']
                                feedback_form.question_set.create(question_text=fbform.cleaned_data['question_1'])
                                feedback_form.question_set.create(question_text=fbform.cleaned_data['question_2'])
                                feedback_form.question_set.create(question_text=fbform.cleaned_data['question_3'])
                                feedback_form.question_set.create(question_text=fbform.cleaned_data['question_4'])
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
                        return HttpResponseRedirect('/instructor/feedbackformadded/')
                #elif esform.is_valid():
                 #       course_set=Course.objects.filter(course_code=esform.cleaned_data['course_code'])
                  #      if not course_set.exists():
                   #             acform=AddCourses()
                    #            esform=EnrollStudents()
                     #           error='Course does not exist'
                      #          return render(request, 'hello_world/home.html',{'course_list':course_list, 'student_list':student_list, 'add_course_form': acform, 'error_esform':error, 'enroll_student_form': esform})
                       # student_set=Student.objects.filter(roll_no=esform.cleaned_data['student_roll_no'])
                        #if not student_set.exists():
                         #       acform=AddCourses()
                          #      esform=EnrollStudents()
                           #     error='Student is not enrolled'
                            #    return render(request, 'hello_world/home.html',{'course_list':course_list, 'student_list':student_list, 'add_course_form': acform, 'error_esform':error, 'enroll_student_form': esform})
                        #for course in course_set:
                         #       for student in student_set:
                          #              course.enrolled_student.add(student)
                        #return HttpResponseRedirect('/admin/studentenrolled/')

    # if a GET (or any other method) we'll create a blank form
        else:
                fbform = AddCourseFeedback()
                #esform = EnrollStudents()

        
        return render(request,'instructor/home.html', {'feedback_form':fbform})

def instructoradded(request):
        return render(request,'instructor/instructoradded.html')

def feedbackformadded(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/instructor/')
        return render(request,'instructor/feedbackformadded.html')
        
def logout_page(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/instructor/')
        logout(request)
        return render(request,'instructor/logout.html')