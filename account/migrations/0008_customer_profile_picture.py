# Generated by Django 3.1.4 on 2020-12-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
