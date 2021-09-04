from django.db import models
from new_agre.models import Rooms
from django.contrib.auth.models import User



class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
    	return str(self.username) + str(self.room)

class Confirm_fill(models.Model):
	Room_nme=models.ForeignKey(Rooms,related_name='client_or_Service', on_delete=models.CASCADE,blank=True,null=True)
	Client_filled=models.BooleanField(default=False)
	Service_filled=models.BooleanField(default=False)
	Room_owner=models.ForeignKey(User,related_name='room_owen', on_delete=models.CASCADE,blank=True,null=True)
	Asigned=models.ForeignKey(User, related_name='asigned_user',on_delete=models.CASCADE,blank=True,null=True)



	class Meta:
		verbose_name_plural="form filled"

	def __str__(self):
		return str(self.Room_nme) 


class Both_Signed(models.Model):
	Room_nme=models.ForeignKey(Rooms,related_name='client_and_Service', on_delete=models.CASCADE,blank=True,null=True)
	Client_fill=models.BooleanField(default=False)
	Service_fill=models.BooleanField(default=False)


	class Meta:
		verbose_name_plural="Both Signed"

	def __str__(self):
		return str(self.Room_nme) 


class Both_edited(models.Model):
	Room_nme=models.ForeignKey(Rooms,related_name='to_check_edits', on_delete=models.CASCADE,blank=True,null=True)
	Client_fill=models.BooleanField(default=False)
	Service_fill=models.BooleanField(default=False)


	class Meta:
		verbose_name_plural="Both edited"

	def __str__(self):
		return str(self.Room_nme) 