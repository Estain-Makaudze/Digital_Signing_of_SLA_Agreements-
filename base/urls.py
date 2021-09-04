"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views
from django.urls import path
from .views import audit_trial
from django.conf import settings
from django.conf.urls.static import static


app_name='base'
urlpatterns = [

	# Home page
	path('index', views.index, name='index'),
	path('add_info',views.add_info,name='add_info'),
	path('client_info',views.client_info,name='client_info'),
	path('dont_agre',views.dont_agre,name='dont_agre'),
    url(r'^pdf/pdf/(?P<room_name>\w+)/$',audit_trial.as_view(),name='audit_trial'),
	path('services',views.services,name='services'),	
    path('<str:room_nme>/', views.both_signed, name='both_signed'),
    path('l_Do/<str:room_nme>/', views.l_Do, name='l_Do'),
    path('done_or/<str:room_nme>/', views.done_or, name='done_or'),
    path('display_audit/<str:room_name>/', views.display_audit, name='display_audit'),
    path('download/<int:agree_id>', views.download, name='download'),
    path('reset/<str:room_name>/', views.reset, name='reset'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)