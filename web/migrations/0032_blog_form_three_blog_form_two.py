# Generated by Django 4.2.4 on 2023-08-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0031_blog_form_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_form_three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='blog_form_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField()),
            ],
        ),
    ]
