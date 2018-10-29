from django.contrib import admin
from .models import Programa, Radio, HorarioFuncionamento

admin.site.register(Radio)
admin.site.register(HorarioFuncionamento)
admin.site.register(Programa)

# Register your models here.
