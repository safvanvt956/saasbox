# Generated by Django 4.2.4 on 2023-08-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0042_blogblog_delete_blog_form_one_delete_blog_form_three_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogblog',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='blogblog',
            name='message',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogblog',
            name='name',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]
