# Generated by Django 2.1.2 on 2019-07-11 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appWorkShop', '0019_auto_20190711_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tallerprofesor',
            name='id_user',
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appWorkShop.Profesor'),
        ),
    ]