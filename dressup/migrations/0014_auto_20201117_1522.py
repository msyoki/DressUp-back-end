# Generated by Django 3.1.3 on 2020-11-17 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dressup', '0013_auto_20201117_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men', 'Men'), ('Ladies', 'Ladies'), ('Kids', 'Kids')], default='Men', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dressup.profile'),
        ),
    ]
