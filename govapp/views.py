from django.shortcuts import render
from django.db import connection
from django.conf import settings
from .models import New_Project, Pdf_Detail

def index(request):
    with connection.cursor() as cursor:
        lastToOne = New_Project.objects.order_by('-id')
        pdf_LastToOne = Pdf_Detail.objects.order_by('-id')
        cursor.execute("Select Image_url from govapp_New_Project order by id desc limit 5;")
        data = cursor.fetchall()
        imagePath = []
        for a in data:
            imagePath.append(settings.MEDIA_URL + a[0])
        grouped = []
        size = 3
        for i in range(0, len(lastToOne), size):
            grouped.append(lastToOne[i:i+size])
    return render(request, 'index.html', {'imagePath': imagePath, "grouped": grouped , "pdf_LastToOne": pdf_LastToOne})

def about(request):
    return render(request, 'about.html')


def certificate(request):
    with connection.cursor() as cursor:
        cursor.execute("select id, Approved_Projects from govapp_Pdf_Detail where id % 2 = 0")
        even_rows = cursor.fetchall()
        even_name = [{'id': r[0], 'Approved_Projects': r[1]} for r in even_rows]

        cursor.execute("select id, Approved_Projects  from govapp_Pdf_Detail where id % 2 = 1")
        odd_rows = cursor.fetchall()
        odd_name = [{'id': r[0], 'Approved_Projects': r[1]} for r in odd_rows]
    return render(request, 'certificate.html', {'even_name': even_name, 'odd_name': odd_name})
