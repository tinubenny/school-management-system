# Generated by Django 5.1.2 on 2024-10-23 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('total_copies', models.PositiveIntegerField()),
                ('available_copies', models.PositiveIntegerField()),
            ],
        ),
    ]
