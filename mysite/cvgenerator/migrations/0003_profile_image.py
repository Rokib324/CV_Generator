# Generated by Django 5.0.1 on 2024-01-09 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvgenerator', '0002_rename_previous_work_profile_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
