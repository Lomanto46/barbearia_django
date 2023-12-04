from django.contrib import admin

# Register your models here.
from . models import *

# Register your models here.
admin.site.register(Barbeiro)
admin.site.register(Cliente)
admin.site.register(Agenda)
admin.site.register(Horario)
admin.site.register(Agendamento)
admin.site.register(Servico)
admin.site.register(Certificacao)
admin.site.register(Feedback)
admin.site.register(Pedido_servico)