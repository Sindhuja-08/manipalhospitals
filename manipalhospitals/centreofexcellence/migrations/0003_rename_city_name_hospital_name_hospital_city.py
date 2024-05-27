# Generated by Django 5.0.6 on 2024-05-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centreofexcellence', '0002_rename_name_hospital_city_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='city_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='hospital',
            name='city',
            field=models.CharField(choices=[('Bengaluru', 'Bengaluru'), ('Bhubaneswar', 'Bhubaneswar'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Jaipur', 'Jaipur'), ('Kolkata', 'Kolkata'), ('Mangaluru', 'Mangaluru'), ('Mysuru', 'Mysuru'), ('Patiala', 'Patiala'), ('Pune', 'Pune'), ('Salem', 'Salem'), ('Vijayawada', 'Vijayawada')], default='Bengaluru', max_length=100),
        ),
    ]
