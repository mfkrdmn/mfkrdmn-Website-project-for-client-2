from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Projeler(models.Model):
    proje_ismi = models.CharField(max_length=150, blank=True)
    Açıklama = RichTextField(max_length=60000, blank=True)
    Lokasyon = models.CharField(max_length=150, blank=True)
    Lokasyon_kısa = models.CharField(max_length=150, blank=True)
    lokasyon_bilgileri = models.TextField(max_length=200, blank=True)
    image_ana_foto  = models.ImageField(upload_to='proje_ana_foto/',blank = True,null = True)
    video_link = models.CharField(max_length=150, blank=True)
    map = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=50, blank=True)
    sehir = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self) :
        return self.proje_ismi

class resimler(models.Model):
    proje = models.ForeignKey(Projeler,on_delete=models.CASCADE)
    image_ana_foto  = models.ImageField(upload_to='altfoto/',blank = True,null = True)

    def __str__(self) :
        return str(self.proje)


class Blog(models.Model):
    blog_basligi = models.CharField(max_length=150, blank=True)
    yazi_icerigi = RichTextField(max_length=60000, blank=True)
    quote = models.CharField(max_length=450, blank=True)
    blog_ana_foto  = models.ImageField(upload_to='blog_ana_foto/',blank = True,null = True)
    blog_alt_foto1  = models.ImageField(upload_to='blog_alt_foto/',blank = True,null = True)
    blog_alt_foto2  = models.ImageField(upload_to='blog_alt_foto/',blank = True,null = True)
    yazar = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self) :
        return self.blog_basligi
    
class CustomerMessages(models.Model):
    isimSoyisim = models.CharField(max_length=50, blank=True)
    Email = models.CharField(max_length=150, blank=True)
    Telefon = models.CharField(max_length=50, blank=True)
    Konu = models.CharField(max_length=500, blank=True)
    Mesaj = models.CharField(max_length=5000, blank=True)


    def __str__(self) :
        return self.Konu