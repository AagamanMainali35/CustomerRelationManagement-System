# Generated by Django 5.0.7 on 2024-08-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0035_customer_password_customer_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='acount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='username')),
                ('password', models.CharField(max_length=50, null=True, verbose_name='username')),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]
