from django.contrib.auth.models import AbstractBaseUser, AnonymousUser, PermissionsMixin, BaseUserManager, UserManager
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from datetime import datetime

from apps.career.models import Career

class UserManager(BaseUserManager):
    def _create_user(self, name, last_name, image, carrera_id, email, puntaje, anonymous_name, incognit_mode, is_plus,
        creation_date, is_active, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            name = name,
            last_name = last_name,
            image = image,
            carrera_id = carrera_id,
            puntaje = puntaje,
            anonymous_name = anonymous_name,
            incognit_mode = incognit_mode,
            is_plus = is_plus,
            creation_date = creation_date,
            is_active = is_active,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, name, last_name, email, password, creation_date,
        image = 'base.png', carrera_id = 1,puntaje = 0, anonymous_name = '', incognit_mode = False, is_plus = False,
        is_active = True, **extra_fields):

        return self._create_user(name, last_name, image, carrera_id, email, puntaje, anonymous_name, incognit_mode,
        is_plus, creation_date, is_active, password, False, False, **extra_fields)

    def create_superuser(self, password, email, name, last_name, carrera_id = None, image = None,
        creation_date = None, puntaje = 0, anonymous_name = '',
        incognit_mode = False, is_plus = False, is_active = True, **extra_fields):

        return self._create_user(name, last_name, image, carrera_id, email, puntaje, anonymous_name, incognit_mode,
        is_plus,creation_date, is_active, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(blank = True, null = True)
    carrera_id = models.ForeignKey(to=Career, on_delete = RESTRICT, blank=True, null=True)
    email = models.EmailField(unique=True)
    puntaje = models.FloatField()
    anonymous_name = models.CharField(max_length=50)
    incognit_mode = models.BooleanField(default=False)
    is_plus = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_created=True, auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    object = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    REQUIRED_FIELDS = ['name', 'last_name']

    USERNAME_FIELD = 'email'

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name


