from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projelerimiz', views.properties, name='properties'),
    path('projelerimiz/<str:sehir>/', views.sehre_gore_projeler, name='sehre_gore_projeler'),
    path('projelerimiz/durumu/<str:status>/', views.proje_durumuna_gore, name='proje_durumuna_gore'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('blog/<str:blog_basligi>/', views.blog_single, name='blog_single'),
    path('<str:pk>/', views.property_single, name='property_single'),
]