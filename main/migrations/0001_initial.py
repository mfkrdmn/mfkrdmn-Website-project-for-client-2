# Generated by Django 4.0.5 on 2023-06-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rfq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proje_ismi', models.CharField(blank=True, max_length=150)),
                ('Açıklama', models.TextField(blank=True, max_length=600)),
                ('Lokasyon', models.CharField(blank=True, max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='proje_alt_foto/')),
                ('video_link', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
