# Generated by Django 2.0.4 on 2018-06-13 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServerApp', '0003_remove_normaluser_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
