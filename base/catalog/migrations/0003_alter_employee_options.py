# Generated by Django 4.0.4 on 2022-06-08 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_chief_employee_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
    ]
