from django.db import models

# Create your models here.
class New_Project(models.Model):
    Image_url = models.ImageField(upload_to='Projects/', default="null")
    New_update = models.CharField(max_length=50)

    def __str__(self):
        return self.New_update
    
class Pdf_Detail(models.Model):
    Approved_Projects = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='pdfs/')
    Password = models.CharField(max_length=20,null=False)
    User_id = models.CharField(max_length=50, null=False)