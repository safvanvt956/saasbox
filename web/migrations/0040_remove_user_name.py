# Generated by Django 4.2.4 on 2023-08-18 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0039_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
