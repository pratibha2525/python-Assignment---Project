# Generated by Django 4.0.5 on 2022-07-07 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_member_pic_member_vehicle_member_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='about_member',
            new_name='about_me',
        ),
    ]
