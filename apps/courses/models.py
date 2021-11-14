from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=500)
    course_yearInCareer = models.IntegerField()
    course_correlative = models.ManyToManyField('self', blank=True)
    course_itsCorrelativeOf = models.ManyToManyField('self', blank=True)
    course_idCareer = models.ManyToManyField(to ='career.Career', blank=True)
    course_idProfessor = models.ManyToManyField(to = 'professor.Professor', blank=True)
    course_topic = models.ImageField(blank=True, null = True)
    course_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.course_name