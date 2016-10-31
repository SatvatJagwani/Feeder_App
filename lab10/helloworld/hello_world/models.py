from django.db import models
from datetime import datetime
#class Question(models.Model):
#question_text = models.CharField(max_length=200)
#pub_date = models.DateTimeField('date published')
#class Choice(models.Model):
#question = models.ForeignKey(Question, on_delete=models.CASCADE) choice_text = models.CharField(max_length=200)
#votes = models.IntegerField(default=0)

# Create your models here.
class Admin(models.Model):
	login_id_text=models.CharField(max_length=40)
	password=models.CharField(max_length=100)
	def __str__(self):
		return self.login_id_text;
	#def addCourses(coursename,course_code,midsem_exam_date,endsem_exam_date,midsem_course_feedback,endsem_course_feedback):
	#	Course.objects.create(coursename,course_code,midsem_exam_date,endsem_exam_date,midsem_course_feedback,endsem_course_feedback)
	#def enrollStudents(coursename,studentname):


class Instructor(models.Model):
	login_id_text=models.CharField(max_length=40)
	password=models.CharField(max_length=100)
	def __str__(self):
		return self.login_id_text;

class Student(models.Model):
	roll_no=models.CharField(max_length=10)
	branch=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name;

class Course(models.Model):
	name=models.CharField(max_length=100)
	course_code=models.CharField(max_length=10,default='000')
	midsem_exam_date=models.DateTimeField(default=datetime.now())
	endsem_exam_date=models.DateTimeField(default=datetime.now())
	enrolled_student=models.ManyToManyField(Student)
	#midsem_course_feedback
	#endsem_course_feedback
	def __str__(self):
		return self.name;

