# Generated by Django 5.0.6 on 2024-06-21 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_contract_alter_salary_salary_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_images/'),
        ),
    ]