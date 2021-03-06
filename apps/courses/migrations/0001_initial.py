# Generated by Django 3.2.8 on 2021-11-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.CharField(max_length=500)),
                ('course_yearInCareer', models.IntegerField()),
                ('course_topic', models.ImageField(upload_to='')),
                ('course_isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
