# Generated by Django 4.0.5 on 2023-07-05 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_projeler_lokasyon_bilgileri_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeler',
            name='status_ar',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='projeler',
            name='status_en',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
