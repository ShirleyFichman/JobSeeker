# Generated by Django 4.0.3 on 2022-04-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_profile', '0007_alter_personalprofile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
