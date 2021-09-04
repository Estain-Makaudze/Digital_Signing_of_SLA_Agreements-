from django.shortcuts import render
from django.shortcuts import render
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from  django.http import HttpResponseRedirect
from new_agre.models import Rooms
from django.shortcuts import redirect
from new_agre.models import Rooms,Service_Cont_Form,Client_Cont_form,Agreemnets,Agree_edits
from base.models import Company_details,Client_OR
from chat.models import Message,Confirm_fill
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import hashlib
import os

# main page after logining in as a client
@login_required
def index(request):
	all_agree=[]
	Ass_room = Rooms.objects.filter(Asigned=request.user)
	for detail in Ass_room:
		comp_det = Company_details.objects.filter(login_owner=detail.Room_owner)
		for things in comp_det:
			c_name=things.Company_name
		u = Rooms.objects.get(pk=detail.id)
		Agreemnets_data = Agreemnets.objects.filter(Room_nme=u)
		for data in Agreemnets_data:
			confirm=data.Done
		new_me={Ass_room,comp_det,Agreemnets_data}
		all_agree.append(new_me)

	context={'all_agree':all_agree}
	return render(request, 'client_side/display_client.html',{'Ass_room':Ass_room})

#to authenticate to acess the room
@login_required
def agre(request):
	if request.method != 'POST':
		return render(request, 'client_side/room_acess.html')
	else:
		room_nme=request.POST.get('room_name')
		password1=request.POST.get('password1')
		pontential=Rooms.objects.filter(Asigned=request.user)
		x=0
		for user_pass in pontential:
			if user_pass.Room_name == room_nme and user_pass.Room_password1 ==password1:
				x=1
				our_room=Rooms.objects.filter(Room_name=user_pass.Room_name)
				Company_dat = Company_details.objects.filter(login_owner=user_pass.Room_owner)
				break
			else:
				pass
		if x==1:
			return render(request, 'base/client_p.html',{'Company_dat':Company_dat,'our_room':our_room})
		else:
			messages.success(request,"Agreement Room name or Password is incorrect")
			return render(request, 'client_side/room_acess.html')


	return render(request, 'client_side/display_client.html')

#upload file for scanning
def upload_file(request):
	if request.method == 'POST':
		test_me = request.FILES['myfile']
		dig_hash=request.POST.get('Dig_Sig')
		fs = FileSystemStorage()
		filename = fs.save(test_me.name, test_me )
		BLOCKSIZE = 65536
		hasher = hashlib.sha1()
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		path = BASE_DIR + "/media/" + filename
		with open(path, 'rb') as afile:
			buf = afile.read(BLOCKSIZE)
			while len(buf) > 0:
				hasher.update(buf)
				buf = afile.read(BLOCKSIZE)
				z=(hasher.hexdigest())	
		x=0
		y=0
		non=0
		identity=0
		pontential=Rooms.objects.all()
		for user_pass in pontential:
			u = Rooms.objects.get(pk=user_pass.id)
			Agreemnets_data = Agreemnets.objects.filter(Room_nme=u.id)
			for thing in Agreemnets_data:
				if thing.Dig_sig == dig_hash and thing.hash_no == z:
					x=1
					identity=thing.id

				else:
					pass

		#for expired
		Agreements_edits = Agree_edits.objects.all()
		for thing_here in Agreements_edits:
			if thing_here.Dig_sig == dig_hash or thing_here.hash_no==z:
				y=20
				non=thing_here.id
				print(non)
				pontential=Rooms.objects.filter(Room_name=thing_here.Room_nme)
				for user_p in pontential:
					e = Rooms.objects.get(pk=user_p.id)
			else:
				pass


		if x==1:
			messages.success(request,"This is a legit Aggrement form")
			details=Agreemnets.objects.filter(pk=identity)
			return render(request, 'login/main_index.html',{'details':details})
		elif y==20:
			when_edits=Agreemnets.objects.filter(Room_nme=e)
			messages.success(request,"Aggrement form expired")
			return render(request, 'login/main_index.html',{'when_edits':when_edits})
		else:
			messages.success(request,"Aggrement form not recognized")
			return render(request, 'login/main_index.html')



