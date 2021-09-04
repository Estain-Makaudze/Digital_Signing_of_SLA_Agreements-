from django.shortcuts import render
import json
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from  django.http import HttpResponseRedirect
from .models import Message,Confirm_fill,Both_edited
from base.models import Company_details,Client_details,Client_OR
from new_agre.models import Rooms,Client_Cont_form,Service_Cont_Form,Agreemnets,Agree_edits
from new_agre.forms import Rooms_Cred,ServiceP_form_Cred,Client_form_Cred
from django.shortcuts import redirect
import hashlib
import random
import string
import secrets
import os
from django.utils import timezone
from datetime import date

#to edit agreemensts
@login_required
def edit_agreements(request, room_nme):
	x=True
	user_in = Client_OR.objects.filter(login_on=request.user)
	for users in user_in:
		if users.is_client==False:
			x=False
		else:
			pass
	if x==False:
		username=request.user
		name=str(username)
		#retrive room details 
		pontential=Rooms.objects.filter(Room_name=room_nme)
		for user_pass in pontential:
			Asigned=user_pass.Asigned
			u = Rooms.objects.get(pk=user_pass.id)
			Company_dat = Company_details.objects.filter(login_owner=user_pass.Room_owner)
		just_added=Service_Cont_Form.objects.filter(Room_nme=u)
		for i in just_added:
			x=i.id
		the_one=Service_Cont_Form.objects.get(pk=x)
		form = ServiceP_form_Cred(request.POST or None, instance = the_one)
		if form.is_valid():
			#generate agreement id 
			lower = string.ascii_lowercase
			upper = string.ascii_uppercase
			num = string.digits
			all = lower + upper + num
			temp = random.sample(all,5)
			agree_id = "".join(temp)

			#ECHANGE INTO AGREE EDITS
			agreed=Agreemnets.objects.filter(Room_nme=u)
			done_or=Agreemnets.objects.get(Room_nme=u)

			edited=Both_edited.objects.get(Room_nme=u)
			edited.Service_fill=True
			edited.save()

			if edited.Service_fill==True and edited.Client_fill==True:
				done_or.Done=False
				done_or.save()
			else:
				pass
			for test in agreed:
				we_do=Agree_edits.objects.create(

				Agreement_id=agree_id
				,Ex_Signed_pdf=test.Signed_pdf
				,Dig_sig=test.Dig_sig
				,Contr_Dig_sig=test.Contr_Dig_sig
				,Room_nme=u
				,hash_no=test.hash_no
				,date_Service_prov_sign=test.date_Service_prov_sign
				,date_Client_sign=test.date_Client_sign
				,date_edited=date.today())

			we_do.save()
			form.save()

			messages.success(request,('Contract form Edited !'))
			return redirect('chat:display_filled', room_nme=room_nme)
		message = Message.objects.filter(room=room_nme)[0:25]
		return render(request, 'chat/edit.html', {'form':form,'Asigned':Asigned,'room_name': room_nme, 'username': name, 'message': message,'Company_dat':Company_dat})

	else:
		username=request.user
		name=str(username)
		#retrive room details 
		pontential=Rooms.objects.filter(Room_name=room_nme)
		for user_pass in pontential:
			Asigned=user_pass.Asigned
			u = Rooms.objects.get(pk=user_pass.id)
			Company_dat = Company_details.objects.filter(login_owner=user_pass.Room_owner)
		just_added=Client_Cont_form.objects.filter(Room_nme=u)

		for i in just_added:
			x=i.id
		the_one=Client_Cont_form.objects.get(pk=x)

		agreed=Agreemnets.objects.get(Room_nme=u)

		form = Client_form_Cred(request.POST or None, instance = the_one)
		if form.is_valid():
			form.save()

			edited=Both_edited.objects.get(Room_nme=u)
			edited.Client_fill=True
			edited.save()
			
			if edited.Service_fill==True and edited.Client_fill==True:
				agreed.Done=False
				agreed.save()
			else:
				pass
			messages.success(request,('Contract form Edited !'))
			return redirect('chat:display_filled', room_nme=room_nme)
		message = Message.objects.filter(room=room_nme)[0:25]
		return render(request, 'chat/edit.html', {'form':form,'Asigned':Asigned,'room_name': room_nme, 'username': name, 'message': message,'Company_dat':Company_dat})


#to check if the agreemesnt is signed
@login_required
def check_for_chat(request,room_nme):
	pontential=Rooms.objects.filter(Room_name=room_nme)
	for user_pass in pontential:
		u = Rooms.objects.get(pk=user_pass.id)
	agreed=Agreemnets.objects.filter(Room_nme=u)
	for test in agreed:
		if test.Real_Done==False:
			return redirect('chat:master_room', room_nme=room_nme)
		else:
			username=request.user
			name=str(username)
			pontential=Rooms.objects.filter(Room_name=room_nme)
			for user_pass in pontential:
				Asigned=user_pass.Asigned
				Company_dat = Company_details.objects.filter(login_owner=user_pass.Room_owner)
			message = Message.objects.filter(room=room_nme)[0:25]
			messages.success(request,"The Agreement was signed and sealed please concider editing the agreement form to make changes")
			return render(request, 'chat/bad_room.html', {'Asigned':Asigned,'room_name': room_nme, 'username': name, 'message': message,'Company_dat':Company_dat})

#to check if neccasary to edit
@login_required
def check_for_edit(request,room_nme):
	pontential=Rooms.objects.filter(Room_name=room_nme)
	for user_pass in pontential:
		u = Rooms.objects.get(pk=user_pass.id)
	agreed=Agreemnets.objects.filter(Room_nme=u)
	for test in agreed:
		if test.Done==True:
			return redirect('chat:edit_agreements', room_nme=room_nme)
		else:
			username=request.user
			name=str(username)
			pontential=Rooms.objects.filter(Room_name=room_nme)
			for user_pass in pontential:
				Asigned=user_pass.Asigned
				Company_dat = Company_details.objects.filter(login_owner=user_pass.Room_owner)
			message = Message.objects.filter(room=room_nme)[0:25]
			messages.success(request,"This room does not have any contact form to edit please first finish filling the contract form and signing it")
			return render(request, 'chat/we_crazy.html', {'Asigned':Asigned,'room_name': room_nme, 'username': name, 'message': message,'Company_dat':Company_dat})


#acess chat room and filling forms -- both service level and client
@login_required
def master_room(request, room_nme):
	x=True
	user_in = Client_OR.objects.filter(login_on=request.user)
	for users in user_in:
		if users.is_client==False:
			x=False
		else:
			pass
	if x== False:
		if request.method != 'POST':
		# Display blank contract form.
			form = ServiceP_form_Cred	
			username=request.user
			name=str(username)
			#retrive room details 
			pontential=Rooms.objects.filter(Room_name=room_nme)
			for user_pass in pontential:
				Asigned=user_pass.Asigned
				Company_dat = Company_details.objects.filter(login_owner=user_pass.Room_owner)
			message = Message.objects.filter(room=room_nme)[0:25]
			return render(request, 'chat/room.html', {'Asigned':Asigned,'room_name': room_nme, 'username': name, 'message': message,'Company_dat':Company_dat,'form':form})

		else:
			form = ServiceP_form_Cred(data=request.POST)
			if form.is_valid():
				form.save()
				return redirect('chat:display_filled', room_nme=room_nme)

	else:
		if request.method != 'POST':
		# Display blank contract form.
			form = Client_form_Cred	
			username=request.user
			name=str(username)
			#retrive room details 
			pontential=Rooms.objects.filter(Room_name=room_nme)
			for user_pass in pontential:
				Asigned=user_pass.Asigned
				Company_dat = Company_details.objects.filter(login_owner=user_pass.Room_owner)
			message = Message.objects.filter(room=room_nme)[0:25]
			return render(request, 'chat/room.html', {'Asigned':Asigned,'room_name': room_nme, 'username': name, 'message': message,'Company_dat':Company_dat,'form':form})

		else:
			form = Client_form_Cred(data=request.POST)
			if form.is_valid():
				form.save()
				return redirect('chat:display_filled', room_nme=room_nme)
	context = {'form': form}
	return HttpResponse("Navigate Back and enter Correct details")
	
#display agreement room		
@login_required
def display_filled(request,room_nme):
	x=True
	user_in = Client_OR.objects.filter(login_on=request.user)
	for users in user_in:
		if users.is_client==False:
			x=False
		else:
			pass
	if x== False:
		pontential=Rooms.objects.filter(Room_name=room_nme)
		for user_pass in pontential:
			Asigned=user_pass.Asigned
			u = Rooms.objects.get(pk=user_pass.id)
			Company_dat = Company_details.objects.filter(login_owner=user_pass.Room_owner)
		filled_things=Service_Cont_Form.objects.filter(Room_nme=u)
		username=request.user
		name=str(username)
		messages = Message.objects.filter(room=room_nme)[0:25]
		return render(request, 'chat/cl_room.html', {'Asigned':Asigned,'room_name': room_nme, 'username': name, 'messages': messages,'filled_things':filled_things,'Company_dat':Company_dat})
	else:
		pontential=Rooms.objects.filter(Room_name=room_nme)
		for user_pass in pontential:
			Asigned=user_pass.Asigned
			u = Rooms.objects.get(pk=user_pass.id)
			Company_dat = Company_details.objects.filter(login_owner=user_pass.Room_owner)
		filled_things=Client_Cont_form.objects.filter(Room_nme=u)
		username=request.user
		name=str(username)
		messages = Message.objects.filter(room=room_nme)[0:25]
		return render(request, 'chat/cli_room.html', {'Asigned':Asigned,'room_name': room_nme, 'username': name, 'messages': messages,'filled_things':filled_things,'Company_dat':Company_dat})
				
