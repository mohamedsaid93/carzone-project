# Generated by Django 4.1.7 on 2023-08-08 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='created_date_2',
            new_name='last_view',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='created_date_1',
            new_name='updated_date',
        ),
    ]