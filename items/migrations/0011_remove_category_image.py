# Generated by Django 4.2 on 2023-09-02 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
