from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils.translation  import gettext as _
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def home(request):
    projeler = Projeler.objects.all()[:2]
    blog_yazıları = Blog.objects.all()[:4]

    context = {
        'projeler' : projeler,
        'blog_yazıları' : blog_yazıları,
        # 'sehre_gore_projeler' : sehre_gore_projeler
    }
    return render(request, 'home.html', context)

def properties(request):
    projeler = Projeler.objects.all().order_by('-updated_at')
    isting_count = Projeler.objects.count()

    project_list = Projeler.objects.all()
    paginator = Paginator(project_list, 4) # Show 25 project per page

    page = request.GET.get('page')
    try:
        project = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        project = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        project = paginator.page(paginator.num_pages)

    context = {
        'projeler' : projeler,
        'isting_count' : isting_count,
        'project' : project
    }
    return render(request, 'properties.html', context)

def sehre_gore_projeler(request, sehir):
    sehre_gore = Projeler.objects.filter(sehir=sehir)
    

    context = {
        'sehre_gore' : sehre_gore,
     
    }
    return render(request, 'properties_by_city.html', context)

def proje_durumuna_gore(request, status):
    durumuna_gore = Projeler.objects.filter(status=status)
    projeler = Projeler.objects.all()
    
    context = {
        'durumuna_gore' : durumuna_gore,
        'projeler' :projeler
    }
    return render(request, 'properties_by_status.html', context)

def property_single(request,pk):

    project_detail = get_object_or_404(Projeler, proje_ismi=pk)
    project_details = Projeler.objects.filter(proje_ismi=pk)
    resim = resimler.objects.filter(proje = project_detail)
    context = {
        'project_detail' : project_detail,
        'project_details' :project_details,
        "resim":resim
    }

    return render(request, 'property-single.html', context)

def about(request):
    blog_yazıları = Blog.objects.all()[:3]

    context = {
        'blog_yazıları' : blog_yazıları
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == "POST":
        isimSoyisim = request.POST['isimSoyisim']
        Email = request.POST['Email']
        Telefon = request.POST['Telefon']
        Konu = request.POST['Konu']
        Mesaj = request.POST['Mesaj']
        send_email(request,isimSoyisim,Email,Telefon,Konu,Mesaj)
        if request.method == "POST":

            newMessage = CustomerMessages.objects.create(isimSoyisim=isimSoyisim, Email=Email, 
            Telefon=Telefon,Konu=Konu,Mesaj=Mesaj)
            newMessage.save()
            return redirect('/')
        
    return render(request, 'contact.html')

def send_email(request,isimSoyisim,Email,Telefon,Konu,Mesaj):
    plaintext = get_template('email_temp.txt')
    htmly= get_template('email_temp.html')
    
    d = {"isimSoyisim":isimSoyisim,
         "Email":Email,
         "Telefon":Telefon,
         "Konu":Konu,
         "Mesaj":Mesaj,
      }
    
    subject, from_email, to = "Bize Ulaşından gelenler", 'from@example.com', 'to@example.com'
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, ["mfkrdmn@gmail.com"])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    

def blog(request):

    blog_yazıları = Blog.objects.all()

    paginator = Paginator(blog_yazıları, 9) 

    page = request.GET.get('page')
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog = paginator.page(paginator.num_pages)

    context = {
        'blog_yazıları' : blog_yazıları,
        'blog' :blog
    }

    return render(request, 'blog.html', context)

def blog_single(request, blog_basligi):

    blog_detail = Blog.objects.filter(blog_basligi=blog_basligi)
    blog_yazıları = Blog.objects.all()[:3]


    context = {
        'blog_detail' : blog_detail,
        'blog_yazıları' : blog_yazıları,
    }

    return render(request, 'blog-single.html', context)


