# Generated by Django 2.2 on 2019-07-07 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20190707_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='buktiPembayaran',
        ),
    ]
