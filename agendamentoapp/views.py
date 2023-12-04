from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator

    
def clientes(request):
    return render(request, 'agendamentoapp/cliente.html')

@has_role_decorator('barbeiro')
@login_required()
def barbeiro(request):
    return render(request, 'agendamentoapp/barbeiro.html')


@login_required(login_url='logar')
@has_role_decorator('cliente')
def agendar(request):
    barbeiros = Barbeiro.objects.all()
    context = {'barbeiros': barbeiros}
    return render(request, 'agendamentoapp/agendar.html', context)

@has_role_decorator('cliente')
@login_required()
def data(request, id_barbeiro):
    barbeiros = Barbeiro.objects.all()
    barbeiro = get_object_or_404(Barbeiro, pk=id_barbeiro)
    datas = Agenda.objects.filter(barbeiro=id_barbeiro, status=True)
    context = {'barbeiros': barbeiros, 'barbeiro': barbeiro, 'datas': datas}
    return render(request, 'agendamentoapp/agendar.html', context)

@has_role_decorator('cliente')
@login_required()
def horarios(request, id_data):
    data_sele = get_object_or_404(Agenda, pk=id_data)
    barbeiros = Barbeiro.objects.all()
    servicos = Servico.objects.all()
    horarios = data_sele.horario_set.all().filter(ativo=True)
    context = {'barbeiros': barbeiros, 'datasele': data_sele, 'horarios': horarios, 'servicos': servicos}
    return render(request, 'agendamentoapp/agendar.html', context)

@has_role_decorator('cliente')
@login_required()
def criar_pedido(request):
    barbeiros = Barbeiro.objects.all()

    if request.method == 'POST':
        
        horario = request.POST.get('horario')
        hr = get_object_or_404(Horario, id=horario, ativo=True)
        clientee = Cliente.objects.get(user=request.user)
        ag = Agendamento(cliente=clientee, horario=hr)
        ag.save()
        
        servico = request.POST.getlist('servico')
        servicos_sele = Servico.objects.filter(id__in=servico)
        for srv in servicos_sele:
            novo_pedido = Pedido_servico(cliente=clientee ,servico=srv)
            novo_pedido.save()
            ag.servicos.add(novo_pedido)
        ag.save()
        
        hr.ativo = False
        hr.save()
        messages.success(request, 'Agendamento realizado com sucesso!')
        return redirect('principal')
    
@has_role_decorator('barbeiro')
@login_required()
def criar_agenda(request):
    agendas = Agenda.objects.filter(barbeiro__user=request.user, status=True)
    
    if request.method == 'POST':
        data_recebida = request.POST.get('data')
        usuario = request.user.barbeiro.id
                
        data_existe = Agenda.objects.filter(data=data_recebida, barbeiro__user=request.user)
        
        if data_existe:
            messages.warning(request, 'Já existe uma agenda cadastrada com a data informada!')
            return redirect('criar_agenda')
        else:
            barbeiro_id = Barbeiro.objects.get(pk=usuario)
            nova_agenda = Agenda(data=data_recebida, status=True, barbeiro=barbeiro_id)
            nova_agenda.save()
            messages.success(request, 'Agenda criada com sucesso!')
            return redirect('criar_agenda')
    return render(request, 'agendamentoapp/agenda.html', {'agendas':agendas})

@has_role_decorator('barbeiro')
@login_required()
def concluir_agenda(request, agenda_id):
    agenda = get_object_or_404(Agenda, pk=agenda_id)
    if request.method == 'POST':
        agenda.status = False
        agenda.save()
        return redirect('criar_agenda')

@has_role_decorator('barbeiro')
@login_required()
def criar_horario(request, agenda_id):
    agenda = get_object_or_404(Agenda, pk=agenda_id)
    if request.method == 'POST':
        horario_recebido = request.POST.get('horario')
        
        horario_existe = agenda.horario_set.filter(horario = horario_recebido)
        
        if horario_existe:
            messages.warning(request, 'O horário informado já esta cadastrado na agenda!')
            return redirect('criar_horario',agenda_id)
        else:
            data = request.POST.get('data')
            data_id = Agenda.objects.get(pk=data)
            novo_horario = Horario(horario=horario_recebido, ativo=True, data=data_id)
            novo_horario.save()
            messages.success(request, 'Horário adicionado com sucesso!')
            return redirect('criar_horario',agenda_id)
    else:
        horarios = agenda.horario_set.all()
        context = {
            'agenda':agenda, 
            'horarios':horarios
        }
        return render(request, 'agendamentoapp/horario.html', context)



@has_role_decorator('barbeiro')
@login_required()  
def ver_cliente(request, id_horario):
    agendamento = Agendamento.objects.all()
    horario = Agendamento.objects.get(horario = id_horario)
    
    listagem = {
        'hors': horario,
        'agents': agendamento
    }
    return render(request, 'agendamentoapp/clientesviews.html', listagem)

def ver_barbeiro(request, id_barbeiro):
    barbeiro = Barbeiro.objects.get(pk=id_barbeiro)
    return render(request, 'agendamentoapp/funcionarios.html', {'barbeiro':barbeiro})

@has_role_decorator('cliente')
@login_required()
def ver_historico(request):
    historico = Agendamento.objects.filter(cliente__user=request.user)
    print(historico)
    return render(request, 'agendamentoapp/historico.html', {'historico':historico})

# def concluir_horario(request, id_horario):
#     horario = Horario.objects.get(pk=id_horario)
#     if request.method == 'POST':
#         horario.concluido = True
#         horario.save()
#         messages.success(request, 'Concluido com sucesso !')
#         return render(request, 'agendamentoapp/horario.html')

def equipe(request):
    barbeiros = Barbeiro.objects.all().order_by('id')
    listagem = {
        'barbers': barbeiros
        
    }
    return render(request, 'agendamentoapp/funcionarios.html', listagem)

    
def ver_feedback(request):
    feedbacks = Feedback.objects.all()
    listagem = {
        'feedbs': feedbacks
    }
    return render(request, 'agendamentoapp/feedback.html', listagem)

@login_required(login_url='logar')
@has_role_decorator('cliente')
def enviarfeed(request):
    if request.method == 'POST':
        
        feedback = request.POST.get('feedback')
        date = request.POST.get('date')
       
        if len(feedback) <= 8:
            messages.error(request, 'Conteudo muito pequeno')
            return redirect('ver_feedback')
    
        novofeedback = Feedback(nome=request.user, conteudo=feedback)
        novofeedback.save()
        messages.success(request, 'Feedback adicionada com sucesso, obrigado')
        return redirect('ver_feedback')
    else:
        return render(request, 'agendamentoapp/adicionar_feedback.html')
    
#Paginas de Erros
@login_required()
def error_403(request, exception):
    return render(request, 'agendamentoapp/403.html')

def error_404(request, exception):
    return render(request, 'agendamentoapp/404.html')

def error_500(request, exception=None):
    return render(request, 'agendamentoapp/500.html')