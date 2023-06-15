from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def properties(request):
    return render(request, 'properties.html')

def property_single(request):
    return render(request, 'property-single.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')
