from django.contrib import admin
from .models import New_Project, Pdf_Detail
# Register your models here.

class New_ProjectAdmin(admin.ModelAdmin):
    list_display = ('Image_url', 'New_update')

class Pdf_detailAdmin(admin.ModelAdmin):
    list_display = ("Approved_Projects", "pdf", "Password", "User_id")


admin.site.register(New_Project, New_ProjectAdmin)
admin.site.register(Pdf_Detail, Pdf_detailAdmin)
