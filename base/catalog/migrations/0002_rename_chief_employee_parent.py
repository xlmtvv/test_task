# Generated by Django 4.0.4 on 2022-06-07 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='chief',
            new_name='parent',
        ),
    ]