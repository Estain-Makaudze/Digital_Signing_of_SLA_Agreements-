from django.contrib import admin
from .models import Message,Confirm_fill,Both_Signed,Both_edited
# Register your models here.


admin.site.register(Message)
admin.site.register(Confirm_fill)
admin.site.register(Both_Signed)
admin.site.register(Both_edited)



