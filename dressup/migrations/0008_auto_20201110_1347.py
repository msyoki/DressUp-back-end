# Generated by Django 3.1.3 on 2020-11-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressup', '0007_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]