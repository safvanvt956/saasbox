# Generated by Django 4.2.4 on 2023-08-26 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0050_alter_about_icon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Awards',
            new_name='Award',
        ),
        migrations.RenameModel(
            old_name='Business',
            new_name='Busines',
        ),
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
    ]