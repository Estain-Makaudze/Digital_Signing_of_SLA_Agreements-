from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from io import BytesIO
from django.contrib.auth import get_user_model
from  django.http import HttpResponseRedirect
from .forms import Company_Details_Form,Client_Details_Form
from django.contrib import messages 
from .models import Company_details,Client_details,Client_OR
from chat.models import Both_Signed,Both_edited
import secrets
from new_agre.models import Rooms,Service_Cont_Form,Client_Cont_form,Agreemnets,Agree_edits
from django.shortcuts import redirect
import os
import random
import string
from django.utils import timezone
from datetime import date
from django.core.files import File
from django.views.generic import View
from base.utils import render_to_pdf
from django.template.loader import get_template
import hashlib
import random
import string
import mimetypes



#render home page
@login_required
def index(request):
	"""The home page Digital Signing of Agreements and Documents"""
	#return HttpResponse("Hello, world. You're at the Hit 200 index.")

	return render(request, 'base/details.html')

#takes client information
@login_required
def client_info(request):
	if request.method != 'POST':
		form=Client_Details_Form
	else:
		address=request.POST['Client_address']
		first_name=request.POST['Client_fname']
		last_name=request.POST['Client_lname']
		phn_n=request.POST['Client_phn_no']
		isave=Client_details(login_own=request.user,Client_address=address,Client_fname=first_name,Client_lname=last_name,Client_phn_no=phn_n)
		isave.save()
		wesave=Client_OR(login_on=request.user,is_client=True)
		wesave.save()
		messages.success(request,"You've completed the registration process. You can login by entering your details. ")
		return HttpResponseRedirect(reverse('login:login'))
		#return HttpResponseRedirect(reverse('base:services',))
	context = {'form': form}
	return render(request, 'base/client_info.html', context)


#to add info 	
@login_required
def  add_info(request):
	if request.method != 'POST':
		form=Company_Details_Form

	else:
		#generator comapany id name
		lower = string.ascii_lowercase
		upper = string.ascii_uppercase
		num = string.digits
		all = lower + upper + num
		temp = random.sample(all,5)
		com_id = "".join(temp)
        #save room name 
		password=request.POST['Company_website']
		address=request.POST['Company_address']
		name=request.POST['Company_name']
		email=request.POST['Company_email']
		reg_no=request.POST['Company_reg_no']
		director=request.POST['Company_director']
		motto=request.POST['Company_motto']
		phn=request.POST['Company_phn_no']
		summary=request.POST['services_summary']
		ints=Company_details(Company_id=com_id,login_owner=request.user,Company_website=password,Company_address=address,Company_name=name,Company_email=email,Company_reg_no=reg_no,Company_director=director,Company_motto=motto,Company_phn_no=phn,services_summary=summary)
		ints.save()
		wesave=Client_OR(login_on=request.user,is_client=False)
		wesave.save()
		messages.success(request,"You've completed the registration process. You can login by entering your details.  ")
		return HttpResponseRedirect(reverse('login:login'))
	context = {'form': form}
	return render(request, 'base/take_info.html', context)

#to render a home for services providers
@login_required
def services(request):
	Company_dat = Company_details.objects.filter(login_owner=request.user)
	return render(request, 'base/business.html',{'Company_dat':Company_dat})

#planning to reset
@login_required
def reset(request,room_name):
	pontential=Client_OR.objects.all()
	for user_pass in pontential:
			u = Client_OR.objects.get(pk=user_pass.id)
			if u.login_on == request.user and u.is_client==False:
				Company_dat = Company_details.objects.filter(login_owner=request.user)
				return render(request, 'base/business.html',{'Company_dat':Company_dat})
			elif  u.login_on == request.user and u.is_client==True:
				pontential=Rooms.objects.filter(Room_name=room_name)
				for user_pass in pontential:
					our_room=Rooms.objects.filter(Room_name=user_pass.Room_name)
					Company_dat = Company_details.objects.filter(login_owner=user_pass.Room_owner)
				return render(request, 'base/client_p.html',{'Company_dat':Company_dat,'our_room':our_room})



"""
def download(request,room_nm):
	pontential=Rooms.objects.filter(Room_name=room_nm)
	for user_pass in pontential:
		u = Rooms.objects.get(pk=user_pass.id)
	
	Agreemnets_data = 'Estain Makaudze Security Analyst CV.pdf'
	return render(request, 'new_agre/preview.html',{'Agreemnets_data': Agreemnets_data})

"""
#to download a pdf 
@login_required
def download(request, agree_id):
        Agreemnets_data = Agreemnets.objects.filter(id=agree_id)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for things in Agreemnets_data:
        	filename=str(things.Signed_pdf)
        	filepath = BASE_DIR + "/media/" +str(things.Signed_pdf)   
        # Open the file for reading content
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sendi
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response

#to check if the agreement hasent been agreed already
@login_required
def done_or(request,room_nme):
	pontential=Rooms.objects.filter(Room_name=room_nme)
	for user_pass in pontential:
		u = Rooms.objects.get(pk=user_pass.id)
	agreed=Agreemnets.objects.filter(Room_nme=u)
	for test in agreed:
		if test.Done==False:
			return redirect('base:both_signed', room_nme=room_nme)
		else:
			messages.success(request,"The Agreement was signed and sealed please concider editing the agreement form to make changes and to open for signatures make sure your partner have edited his/her Contract form")
			return render(request, 'new_agre/final_cont.html')	


#to check if both of them agree on a docu
@login_required
def both_signed(request,room_nme):
	pontential=Rooms.objects.filter(Room_name=room_nme)
	for user_pass in pontential:
		u = Rooms.objects.get(pk=user_pass.id)
	return render(request, 'client_side/i.html',{'u':pontential})


#create a password for non-repudation
@login_required 
def l_Do(request,room_nme):
	if request.method != 'POST':
		# Display blank registration form.
		return render(request, 'client_side/i.html')
	else:
		password1=request.POST.get('password1')		
		pontential=Rooms.objects.filter(Room_name=room_nme)
		x=0
		for user_pass in pontential:
			if user_pass.Room_name == room_nme and user_pass.Room_password1 ==password1:
				x=1
				break
			else:
				pass
		if x==1:
			#check if it is a client or not
			user_in = Client_OR.objects.filter(login_on=request.user)
			for users in user_in:
				#if user is not a client
				if users.is_client==False:
					for user_pass in pontential:
						u = Rooms.objects.get(pk=user_pass.id)
					inst=Both_Signed.objects.get(Room_nme=u)
					inst.Service_fill=True
					#save the client confirmed the agreement
					inst.save()
					#if both of the have signed 
					if inst.Service_fill==True and inst.Client_fill== True:
						for user_pass in pontential:
							u = Rooms.objects.get(pk=user_pass.id)
						it=Agreemnets.objects.get(Room_nme=u)

						edited=Both_edited.objects.get(Room_nme=u)
						edited.Service_fill=False
						edited.save()
						fake_dig=secrets.token_urlsafe(43)
						dig=secrets.token_urlsafe(8)

						it.date_Service_prov_sign=date.today()
						it.Contr_Dig_sig=dig
						it.Dig_sig=fake_dig
						#save in DB tht the agreement is done
						it.Done=True
						it.Real_Done=True
						it.save()
						return redirect('base:audit_trial', room_name=room_nme)

					#if another person have not yet agreed the terms
					else:
						messages.success(request,"Your Agreement parter havent agreed to terms you have filled")
						return render(request, 'new_agre/final_cont1.html')	

				#if the person is not a service provider
				else:
					for user_pass in pontential:
						u = Rooms.objects.get(pk=user_pass.id)
					inst=Both_Signed.objects.get(Room_nme=u)
					inst.Client_fill=True
					inst.save()
					if inst.Service_fill==True and inst.Client_fill== True:

						edited=Both_edited.objects.get(Room_nme=u)
						edited.Client_fill=False
						edited.save()

						Agree_thing=Agreemnets.objects.get(Room_nme=u)
						Agree_thing.date_Client_sign =date.today()
						Agree_thing.save()
						return redirect('base:display_audit', room_name=room_nme)
					else:
						messages.success(request,"Your Agreement parter havent agreed to terms you have filled")
						return render(request, 'new_agre/final_cont1.html')	

		#if not entering correct passords
		else:
			messages.success(request," Wrong Credentilas Try Again")
			return render(request, 'client_side/i.html')


@login_required
def dont_agre(request):
	messages.success(request,"Please Navigate back to Chat rooom for negotiations with your partner ")
	return render(request, 'base/dont_agree.html')	
				
#to generate a pdf takes hash and save in db
class audit_trial(View):
	def get(self, request,room_name, *args, **kwargs):
		template = get_template('base/pdf.html')
		gd_room=Rooms.objects.filter(Room_name=room_name)
		for user_pass in gd_room:
			Room_ting = Rooms.objects.get(pk=user_pass.id)
		Client_things=Client_Cont_form.objects.filter(Room_nme=Room_ting)
		Service_things=Service_Cont_Form.objects.filter(Room_nme=Room_ting)
		Agree_thing=Agreemnets.objects.get(Room_nme=Room_ting)
		context = {Client_things:'Client_things',Service_things:'Service_things'}
		html = template.render(context)
		pdf = render_to_pdf('base/pdf.html', context)
		if pdf:
			#response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Agreement_"+room_name+".pdf" 
			Agree_thing.Signed_pdf.save(filename, File(BytesIO(pdf.content)))
			Agree_thing.save()
			Agree_ting=Agreemnets.objects.filter(Room_nme=Room_ting)
			BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
			for things in Agree_ting:
				filename=str(things.Signed_pdf)
				filepath = BASE_DIR + "/media/" +str(things.Signed_pdf)
			
			Agree_thing.date_Service_prov_sign =date.today()
			Agree_thing.done=True
			Agree_thing.Dig_sig=secrets.token_urlsafe(55)
			content = "inline; filename='%s'" %(filename)
			BLOCKSIZE = 65536
			hasher = hashlib.sha1()
			with open(filepath, 'rb') as afile:
			    buf = afile.read(BLOCKSIZE)
			    while len(buf) > 0:
			        hasher.update(buf)
			        buf = afile.read(BLOCKSIZE)
			real=hasher.hexdigest()
			Agree_thing.hash_no=real
			Agree_thing.save()
			"""
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
			"""	
			return redirect('base:display_audit', room_name=room_name)
			


#to display audit trial
@login_required
def display_audit(request,room_name):
	pontential=Rooms.objects.filter(Room_name=room_name)
	for user_pass in pontential:
		u = Rooms.objects.get(pk=user_pass.id)
	Agreemnets_data = Agreemnets.objects.filter(Room_nme=u)
	Agreements_edits = Agree_edits.objects.filter(Room_nme=u)
	return render(request, 'new_agre/audit_trial.html',{'Agreemnets_data':Agreemnets_data,'Agreements_edits':Agreements_edits})


#for confirm if the contract form is filled 
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
			
"""
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
			'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='applicationO/pdf')
"""


	





	
	

			