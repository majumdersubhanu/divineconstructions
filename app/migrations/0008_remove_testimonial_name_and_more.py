# Generated by Django 5.0.4 on 2024-05-10 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_testimonial_image_alter_testimonial_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='name',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='occupation',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='testimony',
        ),
    ]
