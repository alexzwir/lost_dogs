# Generated by Django 2.1.2 on 2018-11-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crewlostdog',
            name='crew_avatar_photo',
            field=models.ImageField(blank=True, null=True, upload_to='website/core/uploads/'),
        ),
    ]