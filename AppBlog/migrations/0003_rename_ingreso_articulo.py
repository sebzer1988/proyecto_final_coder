# Generated by Django 4.1.1 on 2022-09-26 13:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppBlog', '0002_ingreso_delete_entrada'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingreso',
            new_name='articulo',
        ),
    ]
