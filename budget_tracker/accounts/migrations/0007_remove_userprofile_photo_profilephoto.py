# Generated by Django 4.2.7 on 2024-03-28 18:53

import budget_tracker.accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userprofile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='photo',
        ),
        migrations.CreateModel(
            name='ProfilePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=budget_tracker.accounts.models.user_directory_path)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]
