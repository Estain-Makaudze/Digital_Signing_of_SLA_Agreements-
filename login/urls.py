from django.conf.urls import url 
from django.contrib.auth.views import LoginView
from . import views
from django.urls import path


app_name='login'

urlpatterns = [
	path('register/',views.register,name='register'),
	path('login/',views.login,name='login'),
	path('',views.main,name='main'),
	url(r'^logout/$', views.logout_view, name='logout'),
]

