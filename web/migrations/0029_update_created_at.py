# Generated by Django 4.2.4 on 2023-08-16 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_alter_awards_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
