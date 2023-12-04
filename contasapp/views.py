from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib import messages, auth
from agendamentoapp.models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rolepermissions.roles import assign_role
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
from agendamentoapp.models import *
from django.contrib.admin import AdminSite

# View para cadastro de usuários
def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome').strip()
        email = request.POST.get('email').strip()
        usuario = request.POST.get('usuario').strip()
        fone = request.POST.get('fone').strip()
        senha = request.POST.get('senha').strip()
        data = request.POST.get('data').strip()
        confsenha = request.POST.get('confsenha').strip()

        if len(nome) < 8:
            messages.error(request, 'Nome muito curto, deve possuir no mínimo 8 caracteres!')
            return redirect('cadastrar')

        #verificando se existe algum usuário com o mesmo username já cadastrado no banco
        verifica_usuario = User.objects.filter(username=usuario)
        if len(verifica_usuario) > 0:
            messages.error(request, 'Já existe um usuário cadastrado no sistema')  
            return redirect('cadastrar')
        
        if len(usuario) < 6:
            messages.error(request, 'O nome de usuário de acesso deve possuir no minímo 6 caracteres!')  
            return redirect('cadastrar')
        
        #verificando se existe algum usuário com o mesmo email já cadastrado no banco
        verifica_email = User.objects.filter(email=email)
        if len(verifica_email) > 0:
            messages.error(request, 'Este email já está em uso, por favor informe outro!')
            return redirect('cadastrar')
        
        if len(senha) < 8:
            messages.error(request, 'A senha deve possuir no mínimo 8 caracteres!') 
            return redirect('cadastrar')

        if senha != confsenha:
             messages.error(request, 'As senhas informadas devem ser iguais!')
             return redirect('cadastrar')

        #criando e salvando o usuário no banco
        usuario_criar = User.objects.create_user(username=usuario, email=email, password=senha)
        usuario_criar.save()
        assign_role(usuario_criar, 'cliente')
        
        #criando e salvando um cliente a partir do usuário anterior
        cliente = Cliente.objects.create(user = usuario_criar, nome_completo = nome, telefone=fone, data_nasc=data)
        cliente.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('cadastrar')
    else:
        return render(request, 'contasapp/cadastro.html')
    
#criando a view de login
def logar(request):
    clientes = Cliente.objects.all()
    barbeiros = Barbeiro.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=nome, password=senha )
        if user:
            if user.is_staff:
                login(request, user)
                return redirect('index')
            for c in clientes:
                if c.user == user:
                    achou = True
                    break
                else:
                    achou = False
            if achou == True:
                login(request, user)
                return redirect('principal')
            else:
                for b in barbeiros:
                    if b.user == user:
                        achou = True
                        break
                    else:
                        achou = False
                if achou == True:
                    login(request, user)
                    return redirect('barbeiro')
                else:
                    messages.error(request, 'Nome ou senha inválidos!')
                    return redirect('logar')
        else:
            messages.error(request, 'Nome ou senha inválidos!')
            return redirect('logar')
    else:
        return render(request, 'contasapp/login.html')
    

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('logar')


#Cadastro de Barbeiro no sistema por meio do Gestor
@has_role_decorator('admin')
@login_required()
def cadastro_barbeiro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confsenha = request.POST.get('confsenha')
        datanascimento = request.POST.get('datanascimento')
        foto = request.FILES.get('barbeirofoto')

        if len(nome) < 8:
            messages.error(request, 'Nome muito curto, deve possuir no mínimo 8 caracteres!')
            return redirect('cad_barbeiro')

        #verificando se existe algum usuário com o mesmo username já cadastrado no banco
        verifica_usuario = User.objects.filter(username=usuario)
        if len(verifica_usuario) > 0:
            messages.error(request, 'O nome ({usuario}) já está cadastrado no sistema!')  
            return redirect('cad_barbeiro')
        
        if len(usuario) < 6:
            messages.error(request, 'O nome de usuário de acesso deve possuir no minímo 6 caracteres!')  
            return redirect('cad_barbeiro')
        
        if len(senha) < 8:
            messages.error(request, 'A senha deve possuir no mínimo 8 caracteres!') 
            return redirect('cad_barbeiro')

        if senha != confsenha:
             messages.error(request, 'As senhas informadas devem ser iguais!')
             return redirect('cad_barbeiro')

        #criando e salvando o usuário no banco
        usuario_criar = User.objects.create_user(username=usuario, password=senha)
        usuario_criar.save()
        assign_role(usuario_criar, 'barbeiro')
        #criando e salvando um cliente a partir do usuário anterior
        barbeiro = Barbeiro.objects.create(user=usuario_criar, nome_completo=nome, data_nasc=datanascimento, imagem=foto)
        barbeiro.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('logar')
    return render(request, "contasapp/cad_barbeiro.html")

#Pagina principal para gerenciamento do Gestor
@has_role_decorator('admin')
@login_required()
def index(request):
    barbeiros = Barbeiro.objects.all()
    return render(request, "contasapp/base_gestor.html", {'barbeiros':barbeiros})



#Paginas de Erros
def error_403(request, exception):
    return render(request, 'contasapp/403.html')

def error_404(request, exception):
    return render(request, 'contasapp/404.html')

def error_500(request, exception=None):
    return render(request, 'contasapp/500.html')