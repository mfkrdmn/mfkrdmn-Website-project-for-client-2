from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties', views.properties, name='properties'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('property_single', views.property_single, name='property_single'),
]