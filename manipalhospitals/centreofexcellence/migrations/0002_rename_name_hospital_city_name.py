# Generated by Django 5.0.6 on 2024-05-27 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centreofexcellence', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='name',
            new_name='city_name',
        ),
    ]
