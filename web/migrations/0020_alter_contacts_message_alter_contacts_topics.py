# Generated by Django 4.2.4 on 2023-08-15 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_contacts_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='Message',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='Topics',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
