# Generated by Django 3.1.2 on 2020-11-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field=207, null=True, upload_to='', width_field=243),
        ),
    ]