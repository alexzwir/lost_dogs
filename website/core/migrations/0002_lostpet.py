# Generated by Django 2.1.2 on 2018-10-14 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LostPet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lost_pet_pointing', models.CharField(max_length=50)),
            ],
        ),
    ]
