# Generated by Django 4.0.5 on 2023-06-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_blog_yazar'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='projeler',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
