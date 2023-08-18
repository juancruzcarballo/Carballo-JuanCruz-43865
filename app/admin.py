from django.contrib import admin
from .models import Vino, Cliente, Marca, Empleado, Avatar


# Register your models here.
admin.site.register(Vino)
admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Empleado)
admin.site.register(Avatar)