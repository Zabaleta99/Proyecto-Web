# Generated by Django 3.1.3 on 2020-11-19 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appRedSocial', '0011_auto_20201118_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
    ]