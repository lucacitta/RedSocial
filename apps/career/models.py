from django.db import models

class Career(models.Model):
    carrer_name = models.CharField(max_length=100)
    carrer_description = models.CharField(max_length=500)
    carrer_years = models.IntegerField()
    carrer_idCourses = models.ManyToManyField(to = 'courses.Course', related_name ='MTM_courses', blank=True)
    carrer_idProfessor = models.ManyToManyField(to ='professor.Professor', related_name ='MTM_professor', blank=True)
    carrer_idSupervisor = models.ForeignKey(to = 'professor.Professor', related_name ='FK_Supervisor', on_delete=models.RESTRICT, blank=True, null=True)
    carrer_programYear = models.IntegerField()
    carrer_isActive = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Career'
        verbose_name_plural = 'Careers'

    def __str__(self):
        return self.carrer_name