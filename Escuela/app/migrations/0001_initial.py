# Generated by Django 4.0.4 on 2022-06-13 19:28

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACTIVIDAD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_actividad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ALUMNO',
            fields=[
                ('rut_alumno', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre_alumno', models.CharField(max_length=100)),
                ('apellido_alumno', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ASIGNATURA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_asigantura', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CURSO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PROFESOR',
            fields=[
                ('rut_profesor', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nombre_profesor', models.CharField(blank=True, max_length=255, null=True)),
                ('apellido_profesor', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EVALUACION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_evaluacion', models.DateField()),
                ('ASIGNATURA', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='DETALLE_JEFATURA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CURSO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('PROFESOR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='DETALLE_EVALUACION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('ALUMNO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
                ('EVALUACION', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.evaluacion')),
            ],
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
        migrations.CreateModel(
            name='CURSA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('ALUMNO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
                ('CURSO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rut', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
