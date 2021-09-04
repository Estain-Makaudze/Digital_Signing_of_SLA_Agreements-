from django.conf.urls import url
from . import views
from django.urls import path

app_name='chat'

urlpatterns = [
    path('display_filled/<str:room_nme>/', views.display_filled, name='display_filled'),
    path('master_room/<str:room_nme>/', views.master_room, name='master_room'),
    path('check_for_chat/<str:room_nme>/', views.check_for_chat, name='check_for_chat'),
    path('check_for_edit/<str:room_nme>/', views.check_for_edit, name='check_for_edit'),
    path('edit_agreements/<str:room_nme>/', views.edit_agreements, name='edit_agreements'),
]