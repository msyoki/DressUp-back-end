# Generated by Django 3.1.3 on 2020-11-20 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dressup', '0022_merge_20201119_1017'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='username',
            new_name='profile',
        ),
    ]
