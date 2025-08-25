from django.shortcuts import render
from .models import Projects
# Create your views here.
def index(request):
    projectData = Projects.objects.all()
    return render(request, 'index.html', {'projectData': projectData})


def about(request):
    return render(request, 'about.html')


def certificate(request):
    return render(request, 'certificate.html')
def delete(request):
    projectData = Projects.objects.all()
    # print(projectData.query)
    return render(request, 'delete.html', {'projectData': projectData})