# Generated by Django 5.0.1 on 2024-01-09 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvgenerator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='previous_work',
            new_name='experience',
        ),
    ]