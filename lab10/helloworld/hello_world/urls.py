from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.login,name='login'),
	url(r'^home',views.home,name='home'),
	url(r'^courses/(?P<code>[A-Za-z0-9]+)', views.course, name='course'),
]