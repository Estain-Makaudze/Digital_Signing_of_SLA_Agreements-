from django.db import models
from django.contrib.auth.models import User
from base.models import Company_details
from django.utils.timezone import now
# Create your models here.


class Rooms(models.Model):
	"""redistration for client users"""
	Room_name=models.CharField(max_length = 20)
	Room_password1=models.CharField(max_length = 15)
	Room_password2=models.CharField(max_length = 15,null=True)
	Room_owner=models.ForeignKey(User,related_name='requests_created', on_delete=models.CASCADE,blank=True,null=True)
	Asigned=models.ForeignKey(User, related_name='requests_asigned',on_delete=models.CASCADE,blank=True,null=True)

	class Meta:
		verbose_name_plural="Registerd Rooms"

	def __str__(self):
		return str(self.Room_name)


class Client_Cont_form(models.Model):
	Room_nme=models.ForeignKey(Rooms,related_name='client', on_delete=models.CASCADE,blank=True,null=True)
	Client_Company_name=models.CharField(max_length = 20,blank=True,null=True)
	Client_main_contact=models.CharField(max_length = 20,blank=True,null=True)
	Client_tel_no=models.CharField(max_length = 20,blank=True,null=True)
	Client_office_hours=models.CharField(max_length = 20,blank=True,null=True)
	Sla_start_date=models.DateTimeField()
	Sla_end_date=models.DateTimeField()
	Client_performance_review=models.CharField(max_length = 900,blank=True,null=True)
	Customer_Requirement1=models.CharField(max_length = 900,blank=True,null=True)
	Customer_Requirement2=models.CharField(max_length = 900,blank=True,null=True)
	Customer_Requirement3=models.CharField(max_length = 900,blank=True,null=True)
	Client_tel_no=models.CharField(max_length = 20,blank=True,null=True)
	Client_service_office_no=models.CharField(max_length = 20,blank=True,null=True)

	class Meta:
		verbose_name_plural="client_Contract_Form"

	def __str__(self):
		return str(self.Client_Company_name) 



class Service_Cont_Form(models.Model):
	"""redistration for client users"""
	Room_nme=models.ForeignKey(Rooms,related_name='service_provider', on_delete=models.CASCADE,blank=True,null=True)
	Company_SP_name=models.ForeignKey(Company_details,related_name='requests_created', on_delete=models.CASCADE,blank=True,null=True)
	Purpose_of_sla=models.CharField(max_length = 900,blank=True,null=True)
	Goal_of_sla=models.CharField(max_length = 900,blank=True,null=True)
	Sla_objectives1=models.CharField(max_length = 900,blank=True,null=True)
	Sla_objectives2=models.CharField(max_length = 900,blank=True,null=True)
	Sla_objectives3=models.CharField(max_length = 900,blank=True,null=True)
	Sla_objectives4=models.CharField(max_length = 900,blank=True,null=True)
	Service_performance_review=models.CharField(max_length = 20,blank=True,null=True)
	Perfomace_review_frequency=models.CharField(max_length = 900,blank=True,null=True)
	Next_Review_date=models.DateTimeField()
	Service_to_supply=models.CharField(max_length = 900,blank=True,null=True)
	Service_Detailed_description1=models.CharField(max_length = 900,blank=True,null=True)
	Service_Detailed_description2=models.CharField(max_length = 900,blank=True,null=True)
	Service_Detailed_description3=models.CharField(max_length = 900,blank=True,null=True)
	Service_Detailed_description4=models.CharField(max_length = 900,blank=True,null=True)
	Service_provider_requirement1=models.CharField(max_length = 900,blank=True,null=True)
	Service_provider_requirement2=models.CharField(max_length = 900,blank=True,null=True)
	Service_provider_requirement3=models.CharField(max_length = 900,blank=True,null=True)
	Service_provider_requirement4=models.CharField(max_length = 900,blank=True,null=True)
	
	class Meta:
		verbose_name_plural="Service_Contract_Form"

	def __str__(self):
		return str(self.Company_SP_name) 

class Agreemnets(models.Model):
	Room_nme=models.ForeignKey(Rooms,related_name='Agree', on_delete=models.CASCADE,blank=True,null=True)
	Signed_pdf= models.FileField(upload_to='', null=True, blank=True)
	Private_key=models.CharField(max_length = 400 ,null=True, blank=True )
	Public_key=models.CharField(max_length = 400,null=True, blank=True)
	Contr_Dig_sig=models.CharField(max_length = 100,null=True, blank=True)
	Dig_sig=models.CharField(max_length = 100,null=True, blank=True)
	Done=models.BooleanField(default=False)
	Real_Done=models.BooleanField(default=False)
	hash_no=models.CharField(max_length = 40,null=True, blank=True)
	date_Service_prov_sign = models.DateTimeField(default=now)
	date_Client_sign = models.DateTimeField(default=now)



	class Meta:
		verbose_name_plural="Agreemnets"

	def __str__(self):
		return str(self.Room_nme)

 
class Agree_edits(models.Model):
	date_Service_prov_sign = models.DateTimeField(default=now)
	Ex_Signed_pdf= models.FileField(upload_to='', null=True, blank=True)
	Contr_Dig_sig=models.CharField(max_length = 100,null=True, blank=True)
	date_Client_sign = models.DateTimeField(default=now)
	date_edited= models.DateTimeField(default=now)
	Agreement_id=models.CharField(max_length = 20,null=True, blank=True)	
	Room_nme=models.ForeignKey(Rooms,related_name='Agree1', on_delete=models.CASCADE,blank=True,null=True)
	hash_no=models.CharField(max_length = 40,null=True, blank=True)
	Dig_sig=models.CharField(max_length = 100,null=True, blank=True)

	


	class Meta:
		verbose_name_plural="Agree_edits"

	def __str__(self):
		return str(self.Room_nme)
