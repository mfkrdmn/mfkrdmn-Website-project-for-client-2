# Generated by Django 4.0.5 on 2023-06-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_projeler_lokasyon_kısa'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeler',
            name='lokasyon_bilgileri',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
