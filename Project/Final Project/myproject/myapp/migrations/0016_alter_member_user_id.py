# Generated by Django 4.0.5 on 2022-07-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_about_me_member_about_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user_id',
            field=models.CharField(max_length=50),
        ),
    ]