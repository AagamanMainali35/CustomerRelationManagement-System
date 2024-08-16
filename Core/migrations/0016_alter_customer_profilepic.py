# Generated by Django 5.0.7 on 2024-08-06 03:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0015_alter_customer_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profilepic',
            field=models.ImageField(default='CoreImages/default_profile_pic.jpg', upload_to='CoreImages/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]
