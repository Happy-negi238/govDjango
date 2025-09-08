from django.db import models

# Create your models here.
class New_Project(models.Model):
    New_update = models.CharField(max_length=50)

    def __str__(self):
        return self.New_update
    
class Pdf_Detail(models.Model):
    Image_url = models.ImageField(upload_to='Projects/', null=True)
    Approved_Projects = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True, default=None)
    Password = models.CharField(max_length=20,null=False, unique=True, db_collation='utf8_bin')
    User_id = models.CharField(max_length=50, null=False, unique=True, db_collation='utf8_bin')
    is_delete = models.SmallIntegerField(default=1, null=False)


class UserData(models.Model):
    userId = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10, unique=True)
