# Generated by Django 3.1.3 on 2020-11-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRedSocial', '0005_auto_20201118_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hora',
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]