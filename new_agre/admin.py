from django.contrib import admin
from .models import Rooms,Client_Cont_form,Service_Cont_Form,Agreemnets,Agree_edits
# Register your models here.


admin.site.register(Rooms)
admin.site.register(Agree_edits)
admin.site.register(Agreemnets)
admin.site.register(Service_Cont_Form)
admin.site.register(Client_Cont_form)









