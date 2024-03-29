# Generated by Django 2.1.2 on 2019-07-11 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appWorkShop', '0011_sugerencias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asistencia', models.AutoField(primary_key=True, serialize=False)),
                ('fechaAsis', models.DateField()),
                ('alumnosAsis', models.ManyToManyField(blank=True, null=True, to='appWorkShop.Alumno')),
                ('profesorCargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appWorkShop.Profesor')),
                ('tallerAsis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appWorkShop.Taller')),
            ],
        ),
    ]
