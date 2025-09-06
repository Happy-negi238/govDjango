from django.contrib import admin
from .models import New_Project, Pdf_Detail, UserData
# Register your models here.

class New_ProjectAdmin(admin.ModelAdmin):
    list_display = ('New_update',)

class Pdf_detailAdmin(admin.ModelAdmin):
    list_display = ("Approved_Projects", "pdf", "Password", "User_id",'Image_url')

class userDataAdmin(admin.ModelAdmin):
    list_display = ('userId', 'user_name', 'phone_no')


admin.site.register(New_Project, New_ProjectAdmin)
admin.site.register(Pdf_Detail, Pdf_detailAdmin)
admin.site.register(UserData, userDataAdmin)
