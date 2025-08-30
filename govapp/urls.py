from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path("about-us/", views.about, name='about-us'),
    path("certificate/", views.certificate, name='certificate'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
