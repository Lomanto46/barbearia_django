from django.urls import path
from . import views

urlpatterns = [
    #pagina cliente
    path('', views.clientes, name='principal'),
    
    #pagina barbeiro
    path('barbeiro/', views.barbeiro, name='barbeiro'),
    path('vercliente/', views.ver_cliente, name='ver_cliente'),
    
    
    
    #urls que só o barbeiro pode acessar
    path('criar_agenda/', views.criar_agenda, name='criar_agenda'),
    path('horario/<int:agenda_id>/', views.criar_horario, name='criar_horario'),
    path('concluir_agenda/<int:agenda_id>/', views.concluir_agenda, name='concluir_agenda'),
    path('ver_cliente/<int:id_horario>/', views.ver_cliente, name='ver_cliente'),
    path('ver_barbeiro/<int:id_barbeiro>/', views.ver_barbeiro, name='ver_barbeiro'),
    
    
    #urls que só o cliente pode acessar
    path('agendar/', views.agendar, name='agendar'),
    path('datas/<int:id_barbeiro>/', views.data, name='datas'),
    path('horarios/<int:id_data>/', views.horarios, name='horarios'),
    path('criar_pedido/', views.criar_pedido, name='criar_pedido'),
    path('ver_historico/', views.ver_historico, name='ver_historico'),
    
    
    #urls que serve para o feedback do barbeiro!
    path('feedbacks/', views.ver_feedback, name='ver_feedback'),
    path('enviarfeed/', views.enviarfeed, name='enviarfeed')
    
]
