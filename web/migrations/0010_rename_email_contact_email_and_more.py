# Generated by Django 4.2.4 on 2023-08-14 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_rename_email_contact_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='full_name',
            new_name='Fullname',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='mobile',
            new_name='Mobile',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='purpose',
            new_name='Purpose',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='selected_date',
            new_name='SelectDate',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='selected_slot',
            new_name='SelectSlot',
        ),
    ]