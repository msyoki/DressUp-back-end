# Generated by Django 3.1.3 on 2020-11-17 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dressup', '0018_auto_20201117_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dressup.profile'),
        ),
    ]
