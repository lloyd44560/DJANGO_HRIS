# Generated by Django 5.0.6 on 2024-06-07 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_department_holiday_notice_settings_employeeleave_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(max_length=100)),
                ('num_of_days', models.PositiveIntegerField()),
                ('request_type', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
