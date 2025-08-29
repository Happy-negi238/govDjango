from django.shortcuts import render
from .models import Projects
from django.db import connection
from django.conf import settings
# Create your views here.
# def index(request):
#     projectData = Projects.objects.all()
#     return render(request, 'index.html', {'projectData': projectData})


def index(request):
    with connection.cursor() as cursor:
        lastToOne = Projects.objects.order_by('-id')
        cursor.execute("Select Image_url from govapp_Projects order by id desc limit 5;")
        data = cursor.fetchall()
        imgagePath = []
        for a in data:
            imgagePath.append(settings.MEDIA_URL + a[0])
        grouped = []
        size = 3
        for i in range(0, len(lastToOne), size):
            grouped.append(lastToOne[i:i+size])
    return render(request, 'index.html', {'grouped': grouped, 'projectData': lastToOne, 'data': imgagePath})

def about(request):
    return render(request, 'about.html')


def certificate(request):
    with connection.cursor() as cursor:
        cursor.execute("select id, Approved_Projects from govapp_Projects where id % 2 = 0")
        even_rows = cursor.fetchall()
        even_name = [{'id': r[0], 'Approved_Projects': r[1]} for r in even_rows]

        cursor.execute("select id, Approved_Projects  from govapp_Projects where id % 2 = 1")
        odd_rows = cursor.fetchall()
        odd_name = [{'id': r[0], 'Approved_Projects': r[1]} for r in odd_rows]




    return render(request, 'certificate.html', {'even_rows': even_name, 'odd_rows': odd_name, })

def delete(request):
    projectData = Projects.objects.all()
    # print(projectData.query)
    return render(request, 'delete.html', {'projectData': projectData})