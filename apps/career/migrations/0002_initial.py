# Generated by Django 3.2.8 on 2021-11-01 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professor', '0001_initial'),
        ('courses', '0001_initial'),
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='carrer_idCourses',
            field=models.ManyToManyField(related_name='MTM_courses', to='courses.Course'),
        ),
        migrations.AddField(
            model_name='career',
            name='carrer_idProfessor',
            field=models.ManyToManyField(related_name='MTM_professor', to='professor.Professor'),
        ),
        migrations.AddField(
            model_name='career',
            name='carrer_idSupervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='MTM_Supervisor', to='professor.professor'),
        ),
    ]
