# Generated by Django 5.0.2 on 2024-03-02 11:55

import datetime
import storages.backends.s3
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=7)),
                ('img', models.ImageField(blank=True, null=True, storage=storages.backends.s3.S3Storage(bucket_name='kisaa', region_name='us-east-1'), upload_to='user/profile')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email Verified')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.            Unselect this instead of deleting accounts.')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2024, 3, 2, 17, 25, 12, 664865), help_text='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-email'],
            },
        ),
    ]
