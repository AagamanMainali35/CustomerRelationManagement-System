# Generated by Django 5.0.7 on 2024-08-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='C_name',
            new_name='c_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Enter Customer Name here'),
        ),
    ]
