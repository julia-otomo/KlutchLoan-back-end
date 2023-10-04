# Generated by Django 4.2.5 on 2023-10-03 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('rateTables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installment_interest', models.IntegerField(null=True)),
                ('installment_interest_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('comission', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('comission_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('installment_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('card_number', models.CharField(max_length=16, null=True)),
                ('desired_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('total_loan', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('contract_type', models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], default='automatic', max_length=10)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitations', to='clients.client')),
                ('installment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='solicitations', to='rateTables.installment')),
                ('rate_table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='solicitations', to='rateTables.ratetable')),
            ],
        ),
    ]