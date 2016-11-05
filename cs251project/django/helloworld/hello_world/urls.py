from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.login_page,name='login'),
	url(r'^home',views.home,name='home'),
	url(r'^logout',views.logout_page,name='logout'),
	url(r'^courses/(?P<code>[A-Za-z0-9]+)', views.course, name='course'),
	url(r'^courseadded',views.courseadded,name='courseadded'),
	url(r'^studentenrolled',views.studentenrolled,name='studentenrolled'),
	url(r'^login_app',views.login_app,name='loginapp'),
	url(r'^register_students',views.register_students,name='register_students'),
]
