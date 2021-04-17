from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import RestricaoForm
from professores.models import Professor
from disciplinas.models import Disciplina
from salas.models import Sala
from turmas.models import Turma

def restricaoCad(request):

    prof = Professor.objects.all()
    disc = Disciplina.objects.all()
    sala = Sala.objects.all()
    turma = Turma.objects.all()

    form = RestricaoForm
    return render(request, 'confcurso/restricoes.html', {'form': form, 'prof' : prof, 'disc' : disc, 'sala' : sala, 'turma' : turma})
  

"""
def restList(request):
    #rest_list = Restricao.objects.all()
    #return render(request, 'confcurso/restlist.html', {'rest_list': rest_list})
    return HttpResponseRedirect('/')

def exibeRestricao(request, id):
    #restricao = get_object_or_404(Restricao, pk=id)
    #return render(request, 'confcurso/exiberestricao.html', {'restricao': restricao})
    return HttpResponseRedirect('/')

def restricaoCad(request):
    form = RestricaoForm
  
    if request.method == 'POST':
        form = RestricaoForm(request.POST)
        if form.is_valid():
            semestre = form.cleaned_data['semestre_atual']
            hora_inicio = form.cleaned_data['hora_inicio']
            hora_fim = form.cleaned_data['hora_fim'] 
            dias_aula = form.cleaned_data['dias_aula']
            n_geracao = form.cleaned_data['n_geracao']
            taxa_mutacao = form.cleaned_data['taxa_mutacao']
            status = form.cleaned_data['status']
            restricao = form.save(commit=True)
            restricao.save()
            return HttpResponseRedirect('/')
    else:
        form = RestricaoForm
    return render(request, 'confcurso/restricoes.html', {'form': form})

def deleteRestricao(request, id):
    #restricao = get_object_or_404(Restricao, pk=id)
    #restricao.delete()
    messages.info(request, 'Configuração deletada com sucesso!')
    return redirect('confcurso/restricaolist.html')

def editaRestricao(request, id):
    #restricao = get_object_or_404(Restricao, pk=id)
    #form = RestricaoForm(instance=restricao)

    if request.method == 'POST':
        #form = RestricaoForm(request.POST, instance=restricao)

        if form.is_valid():
            restricao.save()
            return redirect('/')
        else:
            return render(request, 'confcurso/editarestricao.html', {'form': form, 'restricao': restricao})
        
    else:
        return render(request, 'confcurso/editarestricao.html', {'form': form, 'restricao': restricao})
    return HttpResponseRedirect('/')"""



