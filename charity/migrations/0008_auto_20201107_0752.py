# Generated by Django 3.1.1 on 2020-11-07 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0007_auto_20201107_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='payment_request_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
