# Generated by Django 2.0.4 on 2018-06-13 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServerApp', '0005_auto_20180613_0322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='foodId',
            new_name='food',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='orderId',
            new_name='order',
        ),
    ]
