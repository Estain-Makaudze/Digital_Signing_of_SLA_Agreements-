from django.shortcuts import render
from django.shortcuts import render
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from  django.http import HttpResponseRedirect
from .forms import Rooms_Cred,ServiceP_form_Cred,Client_form_Cred
from .models import Rooms,Service_Cont_Form,Client_Cont_form,Agreemnets,Agree_edits
from chat.models import Confirm_fill,Both_Signed,Both_edited
import secrets
import os
from django.shortcuts import redirect
from base.models import Company_details,Client_OR
from django.utils import timezone
from datetime import date
from django.core.files import File
from django.http import HttpResponse
from django.views.generic import View
from base.utils import render_to_pdf
from django.template.loader import get_template
import hashlib
import random
import string


#creating password by admin
@login_required
def index(request):
	"""The home page Agreements and Documents"""
	#return HttpResponse("New agrrement")
	if request.method != 'POST':
		form=Rooms_Cred
	else:
		global name ,password1,password2
		name = request.POST['Room_name']
		password1=request.POST['Room_password1']
		password2=request.POST['Room_password2']
		if password1==password2:
			messages.success( request,name,password1)
			return HttpResponseRedirect(reverse('new_agre:search_user'))
		else:
			messages.error(request,"Passwords doesn't match")
			return HttpResponseRedirect(reverse('new_agre:index'))
	context = {'form': form}
	return render(request, 'new_agre/create_room.html', context)

#to search user for asigning
@login_required
def search_user(request):
	if request.method == "POST":
		searched=request.POST['searched']
		User=get_user_model()
		user_searched = User.objects.filter(username__contains=searched)
		return render(request, 'new_agre/sign_aggr.html',{'searched':searched,'user_searched':user_searched})
	else:
		return render(request, 'new_agre/sign_aggr.html')	
		
		#return HttpResponse("mapimnda mdra kwete zvekudaro ")	

#to asign work of 
@login_required
def assign_work(request,userid):
	global name ,password1,password2
	name1 = name 
	User=get_user_model()
	u = User.objects.get(pk=userid)
	Rooms.objects.create(Room_name=name1,Room_owner=request.user,Asigned=u,Room_password1=password2)
	pontential=Rooms.objects.filter(Room_name=name1)
	for user_pass in pontential:
		w = Rooms.objects.get(pk=user_pass.id)
		pr=secrets.token_urlsafe(120)
		pb=secrets.token_urlsafe(100)
		dj=secrets.token_urlsafe(55)
		Agreemnets.objects.create(Room_nme=w ,Private_key=pr ,Public_key=pb,Dig_sig=dj)
		Confirm_fill.objects.create(Room_nme=w)
		Both_Signed.objects.create(Room_nme=w)
		Both_edited.objects.create(Room_nme=w)
	messages.success( request,str(name1) +" | "+ str(u) + " has been assiged")
	return render(request, 'new_agre/sign_aggr.html')	


			
#to create template for contract form
@login_required
def create_tpml(request):
	#home of creating templates
	if request.method != 'POST':
		# Display blank contract form.
		form = ServiceP_form_Cred()
	else:
		# Process completed form.
		form = ServiceP_form_Cred(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('new_agre:admin_panel'))
			#return HttpResponseRedirect(reverse('base:index'))
	context = {'form': form}
	return render(request, 'new_agre/template.html', context)


# to confirm l have filled the form
@login_required
def form_filled(request,room_nme):
	user_in = Client_OR.objects.filter(login_on=request.user)
	pontential=Rooms.objects.filter(Room_name=room_nme)
	for user_pass in pontential:
		u = Rooms.objects.get(pk=user_pass.id)
		
	for users in user_in:
		if users.is_client==False:
			inst=Confirm_fill.objects.get(Room_nme=u)
			inst.Service_filled=True
			inst.save()
			return HttpResponseRedirect(reverse('new_agre:admin_panel'))
			
		else:
			inst=Confirm_fill.objects.get(Room_nme=u)
			inst.Client_filled=True
			inst.save()
			return redirect('new_agre:reviews', room_name=room_nme)

#to acess the admin panel by service provider
@login_required
def admin_panel(request):
	if request.method != "POST":
		pontential=Rooms.objects.filter(Room_owner=request.user)
		return render(request, 'new_agre/signed_agre.html',{'pontential':pontential})
	else:
		return render(request, 'new_agre/signed_agre.html')

#to acess revies panel side
@login_required
def reviews(request,room_name):
	if request.method != "POST":
		pontential=Rooms.objects.filter(Room_name=room_name)
		return render(request, 'new_agre/signed_agre.html',{'pontential':pontential})
	else:
		return render(request, 'new_agre/signed_agre.html')		


#to finaliseand confirm filling of the form
@login_required
def finalise(request,room_id):
	pontential=Confirm_fill.objects.filter(Room_nme=room_id)
	for rom in pontential:
		if rom.Client_filled==True and rom.Service_filled== True:
			pontential2=Client_Cont_form.objects.filter(Room_nme=room_id)
			pontential3=Service_Cont_Form.objects.filter(Room_nme=room_id)
			return render(request, 'new_agre/final_cont.html',{'pontential2':pontential2,'pontential3':pontential3})	
		else:
			messages.success(request,"Please ensure both of you have finished filling the contract form")
			return render(request, 'new_agre/final_cont1.html')


