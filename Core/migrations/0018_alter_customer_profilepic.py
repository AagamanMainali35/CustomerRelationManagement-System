# Generated by Django 5.0.7 on 2024-08-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0017_alter_customer_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profilepic',
            field=models.ImageField(default='media\\CoreImages\\default_profile_pic.jpg', upload_to='CoreImages/'),
        ),
    ]
