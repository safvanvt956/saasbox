# Generated by Django 4.2.4 on 2023-08-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0046_delete_blogblog_remove_product_tags_delete_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='icon',
            field=models.CharField(choices=[('bi-app-indicator', 'Mobile Apps'), ('bi-gear', 'Branding'), ('bi-tools', 'WordPress 5.0'), ('bi-pie-chart', 'Digital')], max_length=20),
        ),
    ]