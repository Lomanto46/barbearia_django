
from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.logar, name='logar'),
    path('logout/', views.logout, name='logout'),
    
    #Path direcionadas ao Gestor
    path('cad_barbeiro/', views.cadastro_barbeiro, name='cad_barbeiro'),
    path('gestor/home', views.index, name='index'),

]
