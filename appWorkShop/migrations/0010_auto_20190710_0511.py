# Generated by Django 2.1.2 on 2019-07-10 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appWorkShop', '0009_talleralumno_id_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TallerColegio',
            fields=[
                ('id_TC', models.AutoField(primary_key=True, serialize=False)),
                ('id_user', models.CharField(blank=True, max_length=40, null=True)),
                ('colegioTomado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appWorkShop.Colegio')),
            ],
        ),
        migrations.CreateModel(
            name='TallerProfesor',
            fields=[
                ('id_TP', models.AutoField(primary_key=True, serialize=False)),
                ('id_user', models.CharField(blank=True, max_length=40, null=True)),
                ('profesorTomado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appWorkShop.Profesor')),
            ],
        ),
        migrations.RenameField(
            model_name='talleralumno',
            old_name='id_tomado',
            new_name='id_TA',
        ),
        migrations.RemoveField(
            model_name='taller',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='taller',
            name='colegio',
        ),
        migrations.RemoveField(
            model_name='taller',
            name='profesor',
        ),
        migrations.AddField(
            model_name='tallerprofesor',
            name='tallerTomado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appWorkShop.Taller'),
        ),
        migrations.AddField(
            model_name='tallercolegio',
            name='tallerTomado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appWorkShop.Taller'),
        ),
    ]