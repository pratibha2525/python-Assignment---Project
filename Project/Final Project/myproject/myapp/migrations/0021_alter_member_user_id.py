# Generated by Django 4.0.5 on 2022-07-10 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_member_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]