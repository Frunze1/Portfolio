# Generated by Django 5.0.6 on 2024-08-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_full',
            field=models.ImageField(upload_to='blog/full/', verbose_name='Image Full'),
        ),
    ]
