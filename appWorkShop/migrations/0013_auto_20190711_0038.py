# Generated by Django 2.1.2 on 2019-07-11 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWorkShop', '0012_asistencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='fechaAsis',
            field=models.DateTimeField(),
        ),
    ]
