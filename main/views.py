from django.shortcuts import render,get_object_or_404,redirect
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def properties(request):
    projeler = Projeler.objects.all()
    isting_count = Projeler.objects.count()

    # sehre_gore_projeler = Projeler.objects.filter(sehir=pk)

    context = {
        'projeler' : projeler,
        'isting_count' : isting_count,
        # 'sehre_gore_projeler' : sehre_gore_projeler
    }
    return render(request, 'properties.html', context)

def property_single(request,pk):

    project_detail = get_object_or_404(Projeler, proje_ismi=pk)
    project_details = Projeler.objects.filter(proje_ismi=pk)

    context = {
        'project_detail' : project_detail,
        'project_details' :project_details,
    }

    return render(request, 'property-single.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')
