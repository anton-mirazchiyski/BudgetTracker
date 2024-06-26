# Generated by Django 4.2.7 on 2024-02-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0002_income_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='type',
            field=models.CharField(choices=[('Earned Income', 'Earned Income'), ('Passive Income', 'Passive Income'), ('Portfolio Income', 'Portfolio Income')], default='Earned Income', max_length=30),
            preserve_default=False,
        ),
    ]
