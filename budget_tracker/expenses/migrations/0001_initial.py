# Generated by Django 4.2.7 on 2024-02-25 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_userprofile_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('currency', models.CharField(blank=True, max_length=30)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]
