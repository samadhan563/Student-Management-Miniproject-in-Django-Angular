# Generated by Django 3.2.5 on 2021-07-21 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_userprofile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='userName',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='password',
            new_name='lastName',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dateOfBirth',
            field=models.DateField(default=None, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='emaiId',
            field=models.CharField(default=None, max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobileNumber',
            field=models.CharField(default=None, max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.CharField(default=None, max_length=200),
        ),
    ]