# Generated by Django 5.0.7 on 2024-08-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0031_alter_customer_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profilepic',
            field=models.ImageField(default='../media/CoreImages/Default.jpg', null=True, upload_to='CoreImages'),
        ),
    ]
