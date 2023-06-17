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
    image_alt_foto1  = models.ImageField(upload_to='proje_alt_foto/',blank = True,null = True)
    image_alt_foto2  = models.ImageField(upload_to='proje_alt_foto/',blank = True,null = True)
    image_alt_foto3  = models.ImageField(upload_to='proje_alt_foto/',blank = True,null = True)
    image_alt_foto4  = models.ImageField(upload_to='proje_alt_foto/',blank = True,null = True)
    image_alt_foto5  = models.ImageField(upload_to='proje_alt_foto/',blank = True,null = True)
    image_alt_foto6  = models.ImageField(upload_to='proje_alt_foto/',blank = True,null = True)
    video_link = models.CharField(max_length=150, blank=True)
    map = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=50, blank=True)
    sehir = models.CharField(max_length=50, blank=True)

    def __str__(self) :
        return self.proje_ismi
