from django.db import models
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
	#def addCourses(coursename):


class Instructor(models.Model):
	login_id_text=models.CharField(max_length=40)
	password=models.CharField(max_length=100)
	def __str__(self):
		return self.login_id_text;

class Course(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name;