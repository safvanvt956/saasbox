# Generated by Django 4.2.4 on 2023-08-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_alter_contacts_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='Message',
            field=models.TextField(null=True),
        ),
    ]