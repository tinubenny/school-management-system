# Generated by Django 5.1.2 on 2024-10-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('staff', 'Office Staff'), ('librarian', 'Librarian')], default='staff', max_length=10),
        ),
    ]
