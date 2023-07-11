from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils.translation  import gettext as _
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.utils.translation  import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation  import gettext as _
from django.utils.translation import get_language, activate, gettext

def dil_bilgisi():
    return get_language()
def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('Hello')

    finally:
        activate(cur_language)
    return text
def home(request):
    projeler = Projeler.objects.all()[:2]
    blog_yazıları = Blog.objects.all()[:4]
    trans = translate(language='en')
    context = {"trans":trans,"dil":dil_bilgisi(),
        'projeler' : projeler,
        'blog_yazıları' : blog_yazıları,
        # 'sehre_gore_projeler' : sehre_gore_projeler
    }
    return render(request, 'home.html', context)



def properties(request):
    projeler = Projeler.objects.all().order_by('-id')
    isting_count = Projeler.objects.count()
    trans = translate(language='en')

    paginator = Paginator(projeler, 4) # Show 25 project per page

    page = request.GET.get('page')
    try:
        projeler = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projeler = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        projeler = paginator.page(paginator.num_pages)
    link = "projelerimiz"
    context = {
        "trans":trans,"dil":dil_bilgisi(),
        'projeler' : projeler,
        'isting_count' : isting_count,
        'link' : link
    }

    projects_searched = None


    if request.GET:
        key = request.GET.get("key")
        if key:
            key_upper = str(key).capitalize().replace("I","İ")
            projects_searched = Projeler.objects.filter(proje_ismi__icontains=key_upper)
            isting_count = Projeler.objects.filter(proje_ismi__icontains=key_upper).count()
            context["project"] = projects_searched
            context['isting_count'] = isting_count
            paginator = Paginator(projects_searched, 4) # Show 25 project per page

            page = request.GET.get('page')
            try:
                projeler = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                projeler = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                projeler = paginator.page(paginator.num_pages)
            context ['projeler'] =projeler
        else:
            context["project"] = projeler  # Tüm içeriği göster
    else:
        context["project"] = projeler  # Tüm içeriği göster

    return render(request, 'properties.html', context)

def sehre_gore_projeler(request, sehir):
    sehre_gore = Projeler.objects.filter(sehir=sehir).order_by('-id')
    sehir = sehir
    trans = translate(language='en')
    paginator = Paginator(sehre_gore, 4) # Show 25 project per page
    isting_count = sehre_gore.count()

    page = request.GET.get('page')
    try:
        sehre_gore = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sehre_gore = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sehre_gore = paginator.page(paginator.num_pages)
    link = "projelerimiz"+str(sehir)
    context = {
        "trans":trans,"dil":dil_bilgisi(),
        'sehre_gore' : sehre_gore,
        'project' : sehre_gore,
        'sehir' : sehir,
        'link' : link,
        'isting_count' : isting_count

    }

    if request.GET:
        key = request.GET.get("key")
        if key:
            key_upper = key.upper()
            projects_searched = Projeler.objects.filter(proje_ismi__icontains=key_upper)
            context["project"] = projects_searched
        else:
            context["project"] = sehre_gore  # Tüm içeriği göster
    else:
        context["project"] = sehre_gore  # Tüm içeriği göster

    return render(request, 'properties_by_city.html', context)

def proje_durumuna_gore(request, status):
    durumuna_gore = Projeler.objects.filter(status=status).order_by('-id')
    projeler = Projeler.objects.all()
    isting_count = durumuna_gore.count()
    status = status
    trans = translate(language='en')
    paginator = Paginator(durumuna_gore, 4) # Show 25 project per page

    page = request.GET.get('page')
    try:
        project = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        project = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        project = paginator.page(paginator.num_pages)
    link = "projelerimiz/durumu/"+str(status)
    context = {
        "trans":trans,"dil":dil_bilgisi(),
        'durumuna_gore' : durumuna_gore,
        'projeler' :projeler,
        'project' : project,
        'status' : status,
        'link' : link,
        'isting_count' : isting_count
    }
    return render(request, 'properties_by_status.html', context)

def property_single(request,pk):
    trans = translate(language='en')
    project_detail = get_object_or_404(Projeler, proje_ismi=pk)
    project_details = Projeler.objects.filter(proje_ismi=pk)
    resim = resimler.objects.filter(proje = project_detail)

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
    link = "propertysingle/"+str(pk)

    context = {
        "trans":trans,"dil":dil_bilgisi(),
        'project_detail' : project_detail,
        'project_details' :project_details,
        "resim":resim,
        "link" : link
    }

    return render(request, 'property-single.html', context)

def about(request):
    blog_yazıları = Blog.objects.all()[:3]
    trans = translate(language='en')
    link = "about"
    context = {
        "trans":trans,"dil":dil_bilgisi(),
        'blog_yazıları' : blog_yazıları,
        'link' : link
    }
    return render(request, 'about.html', context)

def contact(request):
    trans = translate(language='en')
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

    context = {
        "trans":trans,"dil":dil_bilgisi(),
    }

    return render(request, 'contact.html', context)

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
    msg = EmailMultiAlternatives(subject, text_content, from_email, ["info@landinvestgroup.com.tr"])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def blog(request):

    blog_yazıları = Blog.objects.all()

    paginator = Paginator(blog_yazıları, 9)
    trans = translate(language='en')
    link = "blog"
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
        'blog_yazıları' : blog_yazıları,
        'project' :project,
        "trans":trans,"dil":dil_bilgisi(),
        'link' :link
    }

    return render(request, 'blog.html', context)

def blog_single(request, blog_basligi):

    blog_detail = Blog.objects.filter(blog_basligi=blog_basligi)
    blog_yazıları = Blog.objects.all()[:3]
    trans = translate(language='en')
    link = "blog/"+str(blog_basligi)+"/"
    context = {
        'blog_detail' : blog_detail,
        'blog_yazıları' : blog_yazıları,
        "trans":trans,"dil":dil_bilgisi(),
        'link' : link,
    }

    return render(request, 'blog-single.html', context)
def page_not_found_view(request, exception):
    return render(request, '404.html')