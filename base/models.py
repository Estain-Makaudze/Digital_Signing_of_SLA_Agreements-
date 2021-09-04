from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User



# Create your models here.

#model for company registration
class Company_details(models.Model):
	"""redistration for service provides users"""
	login_owner=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
	Company_id=models.CharField(max_length = 5)
	Company_website=models.CharField(max_length = 30,blank=True,null=True,default="")
	Company_address=models.CharField(max_length = 80)
	Company_name=models.CharField(max_length = 20)
	Company_email=models.EmailField()
	Company_reg_no=models.CharField(max_length = 10,)
	Company_director=models.CharField(max_length = 40,)
	Company_motto=models.CharField(max_length = 40,)
	Company_phn_no=models.CharField(max_length = 15,)
	services_summary=models.CharField(max_length = 900)

	class Meta:
		verbose_name_plural="Companies database"

	def __str__(self):
		return str(self.Company_reg_no) +" -" + str(self.Company_name)


class Client_details(models.Model):
	"""redistration for client users"""
	login_own=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,default="")
	Client_address=models.CharField(max_length = 80)
	Client_lname=models.CharField(max_length = 20)
	Client_fname=models.CharField(max_length = 20)
	Client_phn_no=models.CharField(max_length = 15)

	class Meta:
		verbose_name_plural="Client database"

	def __str__(self):
		return str(self.login_own) +" -" + str(self.Client_lname)

class Client_OR(models.Model):
	"""redistration for client users"""
	login_on=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
	is_client=models.BooleanField(default=True)

	class Meta:
		verbose_name_plural="Client OR"

	def __str__(self):
		return str(self.login_on) +" -" + str(self.is_client)


