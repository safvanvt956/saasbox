# Generated by Django 4.2.4 on 2023-08-14 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_rename_date_contact_selectdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='SelectSlot',
            field=models.TimeField(null=True),
        ),
    ]