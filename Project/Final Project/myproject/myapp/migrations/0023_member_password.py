# Generated by Django 4.0.5 on 2022-07-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_remove_member_user_id_member_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
    ]