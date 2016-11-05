from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.login_page,name='login'),
	url(r'^instructoradded',views.instructoradded,name = 'instructoradded'),
	url(r'^home',views.home,name = 'home'),
	url(r'^logout',views.logout_page,name = 'logout'),
	#url(r'^home',views.home,name='home'),
	#url(r'^logout',views.logout_page,name='logout'),
	#url(r'^courses/(?P<code>[A-Za-z0-9]+)', views.course, name='course'),
	url(r'^feedbackformadded',views.feedbackformadded,name='feedbackformadded'),
	url(r'^assignmentdeadlineadded',views.assignmentdeadlineadded,name='assignmentdeadlineadded'),
	#url(r'^login_app',views.login_app,name='loginapp'),
]
