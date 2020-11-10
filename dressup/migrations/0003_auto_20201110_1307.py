# Generated by Django 3.1.3 on 2020-11-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dressup', '0002_auto_20201110_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contact',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]