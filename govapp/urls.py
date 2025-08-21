from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about-us/", views.about, name='about-us'),
    path("certificate/", views.certificate, name='certificate'),
    path("normal/", views.normal, name="try")
]
