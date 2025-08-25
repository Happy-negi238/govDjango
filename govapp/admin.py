from django.contrib import admin
from .models import Projects
# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('Image_url','Approved_Projects', 'New_Projects')
    
admin.site.register(Projects, ProjectsAdmin)
