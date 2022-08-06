# Generated by Django 4.0.5 on 2022-07-09 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_member_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pic', models.FileField(null=True, upload_to='media/images/')),
                ('video', models.FileField(null=True, upload_to='media/images/')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='pic',
        ),
        migrations.AddField(
            model_name='member',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Notice_view',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_at', models.DateTimeField(auto_now_add=True)),
                ('notice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.notice')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
    ]
