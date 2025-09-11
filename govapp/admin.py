from django.contrib import admin
from .models import New_Project, Pdf_Detail, UserData
from admin_extra_buttons.api import ExtraButtonsMixin, button
from django.urls import reverse
from django.http import HttpResponseRedirect
# Register your models here.

class New_ProjectAdmin(admin.ModelAdmin):
    list_display = ('New_update',)

class Pdf_detailAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ("Approved_Projects", "pdf", "Password", "User_id",'Image_url', 'created_at')
    @button(label="Refresh")
    def refresh_callable(self, request):
        self.message_user(request, "refresh called")
        # use reverse with a view name, not raw URL
        return HttpResponseRedirect("/")

class userDataAdmin(admin.ModelAdmin):
    list_display = ('userId', 'user_name', 'phone_no')


admin.site.register(New_Project, New_ProjectAdmin)
admin.site.register(Pdf_Detail, Pdf_detailAdmin)
admin.site.register(UserData, userDataAdmin)
