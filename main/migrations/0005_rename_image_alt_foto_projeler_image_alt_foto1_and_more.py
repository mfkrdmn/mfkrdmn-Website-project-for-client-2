# Generated by Django 4.0.5 on 2023-06-17 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_projeler_image_alt_foto2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeler',
            old_name='image_alt_foto',
            new_name='image_alt_foto1',
        ),
        migrations.AddField(
            model_name='projeler',
            name='image_alt_foto3',
            field=models.ImageField(blank=True, null=True, upload_to='proje_alt_foto/'),
        ),
        migrations.AddField(
            model_name='projeler',
            name='image_alt_foto4',
            field=models.ImageField(blank=True, null=True, upload_to='proje_alt_foto/'),
        ),
        migrations.AddField(
            model_name='projeler',
            name='image_alt_foto5',
            field=models.ImageField(blank=True, null=True, upload_to='proje_alt_foto/'),
        ),
        migrations.AddField(
            model_name='projeler',
            name='image_alt_foto6',
            field=models.ImageField(blank=True, null=True, upload_to='proje_alt_foto/'),
        ),
    ]
