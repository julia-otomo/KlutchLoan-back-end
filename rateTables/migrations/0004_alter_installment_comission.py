# Generated by Django 4.2.5 on 2023-10-04 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateTables', '0003_ratetable_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installment',
            name='comission',
            field=models.FloatField(),
        ),
    ]
