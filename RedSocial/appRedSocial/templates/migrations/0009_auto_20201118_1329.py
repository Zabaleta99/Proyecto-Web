# Generated by Django 3.1.3 on 2020-11-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRedSocial', '0008_auto_20201118_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fotoPerfil',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
