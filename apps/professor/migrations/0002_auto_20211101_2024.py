# Generated by Django 3.2.8 on 2021-11-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
        ('career', '0002_initial'),
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='professor_idCareer',
            field=models.ManyToManyField(null=True, to='career.Career'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='professor_idCourses',
            field=models.ManyToManyField(null=True, to='courses.Course'),
        ),
    ]
