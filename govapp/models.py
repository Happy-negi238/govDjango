from django.db import models

# Create your models here.
class Projects(models.Model):
    Image_url = models.ImageField(upload_to='projects/');
    Approved_Projects = models.TextField();
    New_Projects = models.TextField();