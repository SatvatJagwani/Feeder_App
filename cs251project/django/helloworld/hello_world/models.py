from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
#class Admin(models.Model):
#	login_id_text=models.CharField(max_length=40)
#	password=models.CharField(max_length=100)
#	def __str__(self):
#		return self.login_id_text;
	#def addCourses(coursename,course_code,midsem_exam_date,endsem_exam_date,midsem_course_feedback,endsem_course_feedback):
	#	Course.objects.create(coursename,course_code,midsem_exam_date,endsem_exam_date,midsem_course_feedback,endsem_course_feedback)
	#def enrollStudents(coursename,studentname):


class AdminOrInstructor(models.Model):
	#social_login=models.CharField(max_length=40)
	#username=models.CharField(max_length=40)
	#password=models.CharField(max_length=100)
	#email=models.CharField(max_length=100)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	type=models.CharField(max_length=20,default='instructor')
	#def __str__(self):
	#	return self.user.username;

class Student(models.Model):
	roll_no=models.CharField(max_length=10)
	password=models.CharField(max_length=100)
#	branch=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name;

class Course(models.Model):
	name=models.CharField(max_length=100)
	course_code=models.CharField(max_length=10,default='000')
	#midsem_exam_date=models.DateTimeField(default=datetime.now())
	#endsem_exam_date=models.DateTimeField(default=datetime.now())
	enrolled_student=models.ManyToManyField(Student)
	#midsem_course_feedback
	#endsem_course_feedback
	def __str__(self):
		return self.name;

class FeedbackForm(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,default='feedback')
    deadline=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name;

class AssignmentDeadline(models.Model):
    name=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    deadline=models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name;

class Question(models.Model):
    form=models.ForeignKey(FeedbackForm, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text;

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    frequency = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text;
