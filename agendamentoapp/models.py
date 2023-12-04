from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
    
      
class Barbeiro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=90)
    data_nasc = models.DateField()
    imagem = models.ImageField(blank=True, null=True, upload_to='media')
    
    def __str__(self):
        return f' {self.id}-{self.nome_completo}'

class Feedback(models.Model):
    nome = models.CharField(max_length=50)
    conteudo = models.TextField(max_length=120)
    data = models.DateField(default=timezone.now)
    
    
class Certificacao(models.Model):
    descricao = models.CharField(max_length=90)
    arquivo = models.FileField(upload_to='arquivos')
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.descricao


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=90)
    telefone = models.CharField(max_length=15)
    data_nasc = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo

class Servico(models.Model):
    tipo = models.CharField(max_length=30)
    descricao = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.tipo
    
class Pedido_servico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    

class Agenda(models.Model):
    data = models.DateField()
    status = models.BooleanField(default=True)
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)


class Horario(models.Model):
    horario = models.TimeField()
    ativo = models.BooleanField(default=True)
    concluido = models.BooleanField(default=False)
    data = models.ForeignKey(Agenda, on_delete=models.CASCADE)


class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Pedido_servico)
    finalizado = models.BooleanField(default=False)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Barbeiro: {self.horario.data.barbeiro} ### Cliente: {self.cliente.nome_completo}'



