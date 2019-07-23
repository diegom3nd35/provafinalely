from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    dados ={
        'Pessoas': Pessoa.objects.all(),
        'Tarefas': Tarefa.objects.all()
    }
    if (request.method == 'POST'):
        descricao = request.POST['descricao']
        pessoa_id = request.POST['pessoa']
        pessoa = Pessoa.objects.get(id=pessoa_id)
        tarefa = Tarefa(descricao=descricao, pessoa=pessoa)
        tarefa.save()
       
    return render(request, 'index.html', dados)

def finalizar(request, id_tarefa):
    tarefa = Tarefa.objects.get(id=id_tarefa)
    tarefa.concluida = True
    tarefa.save()
    dados ={
        'Pessoas': Pessoa.objects.all(),
        'Tarefas': Tarefa.objects.all()
    }    

    return render(request, 'index.html', dados)