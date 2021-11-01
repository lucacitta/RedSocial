from django.db import models

class Professor(models.Model):
    professor_id = models.IntegerField(primary_key=True)
    professor_name = models.CharField(max_length=20)
    professor_lastName = models.CharField(max_length=20)
    professor_idCourses = models.ManyToManyField(to = 'courses.Course', default=1)
    professor_rank = models.FloatField()
    professor_isSupervisor = models.BooleanField()
    professor_idCareer = models.ManyToManyField(to = 'career.Career', default=1)
    professor_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

    def __str__(self):
        return self.professor_name