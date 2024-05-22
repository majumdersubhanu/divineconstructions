# Generated by Django 5.0.4 on 2024-05-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_testimonial_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='team_members/')),
            ],
        ),
    ]