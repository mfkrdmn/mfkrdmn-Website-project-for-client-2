from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projelerimiz', views.properties, name='properties'),
    # path('projelerimiz/<str:pk>/', views.properties, name='properties'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('<str:pk>/', views.property_single, name='property_single'),
    
]