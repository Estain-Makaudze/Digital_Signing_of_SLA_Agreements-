from django.conf.urls import url
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name='client_side'

urlpatterns = [
	# main page
	path('index',views.index,name='index'),
	path('agre',views.agre,name='agre'),
	url(r'^upload_file/$', views.upload_file, name='upload_file'),

	]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	


