# Generated by Django 4.1.7 on 2023-05-23 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arty', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Membre',
        ),
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
    ]
