# Generated by Django 4.2.7 on 2024-03-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0003_income_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
