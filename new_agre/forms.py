from django import forms
from django.forms import ModelForm
from .models import Rooms,Client_Cont_form,Service_Cont_Form


#comapny details form to fill in
class Rooms_Cred(ModelForm):
	class Meta:
		model=Rooms
		fields =['Room_name','Room_password1','Room_password2']
		
class ServiceP_form_Cred(ModelForm):
	class Meta:
		model=Service_Cont_Form
		fields =['Room_nme','Company_SP_name','Purpose_of_sla','Goal_of_sla','Sla_objectives1','Sla_objectives2','Sla_objectives3',
		'Sla_objectives4','Service_performance_review','Perfomace_review_frequency','Next_Review_date','Service_to_supply','Service_Detailed_description1',
		'Service_Detailed_description2','Service_Detailed_description3','Service_Detailed_description4','Service_provider_requirement1','Service_provider_requirement2','Service_provider_requirement3','Service_provider_requirement4']
				
class Client_form_Cred(ModelForm):
	class Meta:
		model=Client_Cont_form
		fields =['Room_nme','Client_Company_name','Client_main_contact','Client_tel_no','Client_office_hours','Sla_start_date',
		'Sla_end_date','Client_performance_review','Customer_Requirement1','Customer_Requirement2','Customer_Requirement3','Client_tel_no','Client_service_office_no']
				