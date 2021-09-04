from django import forms
from django.forms import ModelForm
from .models import Company_details,Client_details

#comapny details form to fill in
class Company_Details_Form(ModelForm):
	class Meta:
		model=Company_details
		fields= ['Company_website',
		'Company_address','Company_name','Company_email','Company_reg_no',
		'Company_director','Company_motto','Company_phn_no','services_summary']
		
		


class Client_Details_Form(ModelForm):
	class Meta:
		model=Client_details
		fields=['Client_address','Client_lname','Client_fname','Client_phn_no']
		
		