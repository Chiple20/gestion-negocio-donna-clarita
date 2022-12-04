from django.contrib import admin
from .models import Rol, Sucursal, Usuario

# Register your models here.

admin.site.register(Sucursal)
admin.site.register(Rol)
admin.site.register(Usuario)