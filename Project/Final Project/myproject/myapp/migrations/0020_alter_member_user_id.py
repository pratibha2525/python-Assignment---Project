# Generated by Django 4.0.5 on 2022-07-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_member_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user_id',
            field=models.CharField(max_length=30),
        ),
    ]