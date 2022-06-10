# Generated by Django 4.0.4 on 2022-06-10 12:40

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_chief_employee_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='catalog.employee'),
        ),
    ]