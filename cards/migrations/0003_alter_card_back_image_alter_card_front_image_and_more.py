# Generated by Django 4.2.5 on 2023-10-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_card_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='back_image',
            field=models.ImageField(upload_to='loan-images'),
        ),
        migrations.AlterField(
            model_name='card',
            name='front_image',
            field=models.ImageField(upload_to='loan-images'),
        ),
        migrations.AlterField(
            model_name='card',
            name='selfie_image',
            field=models.ImageField(upload_to='loan-images'),
        ),
    ]
