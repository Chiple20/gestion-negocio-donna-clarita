#from asyncio.windows_events import NULL
import string
from django.db import models

#####################################################
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
import random

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Rol(models.Model):
    id_rol = models.IntegerField(db_column='id_rol',primary_key=True)
    cargo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Rol'

        db_table = 'Rol'
    def __str__(self):

        resumenR = "{0}"
        return resumenR.format(self.cargo)


class Sucursal(models.Model):
    id_sucursal = models.IntegerField(db_column='id_sucursal',primary_key=True)
    sucursal = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Sucursal'

        db_table = 'Sucursal'

    def __str__(self):

        resumenS = "{0}"
        return resumenS.format(self.sucursal)

class UsuarioP(BaseUserManager):
    def create_user(self, username, last_name, password, email, **other_fields):

        if not email:
            raise ValueError(_("Debes dar un email"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, last_name, password, email, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_active') is not True:
            raise ValueError('xd')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('xd')

        return self.create_user(username, last_name, password, email, **other_fields)


class Usuario(AbstractUser, PermissionsMixin):
    
    objects = UsuarioP()

    username = models.CharField(max_length=150)  
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(('Email address'), unique=True)
    link = models.CharField(max_length=200)
    id_rol = models.ForeignKey(Rol, db_column='id_rol',null=True, on_delete=models.CASCADE)
    id_sucursal = models.ForeignKey(Sucursal, db_column='id_sucursal',null=True, on_delete=models.CASCADE)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','last_name']

    def __str__(self):
        resumen = "{0} {1} {2} {3}"
        return resumen.format(self.username,self.last_name, self.email, self.id_rol)
    
    def save(self, *args, **kwargs):
        super(Usuario, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Usuarios_usuario'