# Generated by Django 5.0.6 on 2024-06-07 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_country_field_alter_employee_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_holder_name', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=50)),
                ('account_type', models.CharField(choices=[('S', 'Savings'), ('C', 'Current')], max_length=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_information', to='employee.employee')),
            ],
        ),
    ]