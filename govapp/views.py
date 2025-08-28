from django.shortcuts import render
from .models import Projects
# Create your views here.
# def index(request):
#     projectData = Projects.objects.all()
#     return render(request, 'index.html', {'projectData': projectData})


def index(request):
    projectData = Projects.objects.all()
    grouped = []
    size = 3
    for i in range(0, len(projectData), size):
        grouped.append(projectData[i:i+size])
    return render(request, 'index.html', {'grouped': grouped})

def about(request):
    return render(request, 'about.html')


def certificate(request):
    return render(request, 'certificate.html')

def delete(request):
    projectData = Projects.objects.all()
    # print(projectData.query)
    return render(request, 'delete.html', {'projectData': projectData})