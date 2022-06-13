# Generated by Django 4.0.4 on 2022-06-12 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_actividad_asignatura_cursa_curso_detalle_evaluacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursa',
            name='ALUMNO',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.alumno'),
        ),
        migrations.AddField(
            model_name='cursa',
            name='CURSO',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.curso'),
        ),
        migrations.AddField(
            model_name='detalle_evaluacion',
            name='ALUMNO',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.alumno'),
        ),
        migrations.AddField(
            model_name='detalle_evaluacion',
            name='EVALUACION',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.evaluacion'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='ASIGNATURA',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.asignatura'),
        ),
        migrations.CreateModel(
            name='DETALLE_ACTIVIDAD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_actividad', models.DateField()),
                ('ACTIVIDAD', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.actividad')),
                ('ALUMNO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
            ],
        ),
    ]
