from django.contrib import admin
from .models import Projects, certificate_pdf

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('Image_url','Approved_Projects', 'New_Projects')


class certificate_pdfAmin(admin.ModelAdmin):
    list_display = ('upload_pdf',)

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(certificate_pdf, certificate_pdfAmin)


