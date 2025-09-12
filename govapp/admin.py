from django.contrib import admin
from .models import New_Project, Pdf_Detail, UserData
import uuid

# Register your models here.

class New_ProjectAdmin(admin.ModelAdmin):
    list_display = ('New_update',)

class Pdf_detailAdmin(admin.ModelAdmin):
    list_display = ("Approved_Projects", "pdf", "Password", "User_id",'Image_url', 'created_at')
    change_form_template = "change_form.html"
    def response_change(self,request,obj):
        if "add_custom_userId" in request.POST:
            my_uuid = str(uuid.uuid4())
            print(my_uuid[0:10])
        return super().response_change(request, obj)

class userDataAdmin(admin.ModelAdmin):
    list_display = ('userId', 'user_name', 'phone_no')

admin.site.register(New_Project, New_ProjectAdmin)
admin.site.register(Pdf_Detail, Pdf_detailAdmin)
admin.site.register(UserData, userDataAdmin)
