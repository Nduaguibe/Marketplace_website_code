# Generated by Django 4.2 on 2023-09-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_category_alter_item_options_remove_item_books_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='item_images'),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]