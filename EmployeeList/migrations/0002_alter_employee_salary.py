# Generated by Django 3.2.5 on 2021-07-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
