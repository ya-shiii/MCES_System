# Generated by Django 4.2.6 on 2023-11-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='borrowed',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
