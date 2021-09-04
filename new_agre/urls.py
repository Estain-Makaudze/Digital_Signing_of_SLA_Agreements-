from django.conf.urls import url
from . import views
from django.urls import path



app_name='new_agre'

urlpatterns = [
	# main page

	path('index/',views.index,name='index'),
	path('admin_panel/', views.admin_panel, name='admin_panel'),	
	path('search_user/', views.search_user, name='search_user'),
	path('create_tpml/', views.create_tpml, name='create_tpml'),
    path('<int:room_id>/', views.finalise, name='finalise'),
    path('<str:room_name>/', views.reviews, name='reviews'),
    path('form_filled/<str:room_nme>/', views.form_filled, name='form_filled'),
	url(r'^assign_work/(?P<userid>\w+)/$', views.assign_work, name='assign_work'),


]

