from django.shortcuts import render
from django.db import connection
from django.conf import settings
from .models import New_Project, Pdf_Detail
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PyPDF2 import PdfReader, PdfWriter
import io

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


@csrf_exempt
def check_userId(request):
    if request.method == 'POST':
        User_id = request.POST.get("user_id")
        if Pdf_Detail.objects.filter(User_id=User_id).exists():
            # pdf_url = Pdf_Detail.objects.get(User_id=User_id).pdf
            # pdf_url = pdf_url.url
            return JsonResponse({"status": "success", "message": "User ID valid hai", "download_url": f"/download/{User_id}/"})
        else:
            return JsonResponse({"status": "error", "message": "Enter valid User Id"})
        
def download_pdf(request, user_id):
    try:
        pdf_detail = Pdf_Detail.objects.get(User_id=user_id)
        pdf_path = pdf_detail.pdf.path
        password = pdf_detail.Password

        # Original PDF read karo
        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        # Password protection lagao
        writer.encrypt(user_password=password, owner_password=password)

        # Memory stream me likho
        output = io.BytesIO()
        writer.write(output)
        output.seek(0)

        response = HttpResponse(output, content_type="application/pdf")
        response['Content-Disposition'] = f'attachment; filename="{pdf_detail.Approved_Projects}.pdf"'
        return response

    except Pdf_Detail.DoesNotExist:
        return HttpResponse("Invalid User ID")