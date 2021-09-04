from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import logout, authenticate , login as dj_login
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import auth
from django.contrib import messages
from base.models import Client_OR
from django.contrib.auth.decorators import login_required

#main page with scan docu
def main(request):

	return render(request, 'login/main_index.html')	



def logout_view(request):
	#Log the user out.
	auth.logout(request)
	return render(request, 'login/login.html')	

def login(request):
	if request.method =='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is not None:
			dj_login(request,user)
			user_in = Client_OR.objects.all().filter(login_on=request.user)
			for users in user_in:
				if users.is_client==False:
					return HttpResponseRedirect(reverse('base:services'))
				else:
					return HttpResponseRedirect(reverse('client_side:index'))

		else:
			messages.info(request,'Username OR password is incorrect')
	context ={}
	return render(request, 'login/login.html', context)

def register(request):
	"""Register a new user."""
	if request.method != 'POST':
		# Display blank registration form.
		form = CreateUserForm()
	else:
		# Process completed form.
		form = CreateUserForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			#form = save_user(request.POST)
			#form.save()
			# Log the user in and then redirect to home page.
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])

			dj_login(request, authenticated_user)
			return HttpResponseRedirect(reverse('base:index'))
	context = {'form': form}
	messages.error(request,form.errors  )
	return render(request, 'login/register.html', context)



