from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Disciplina
from .forms import DisciplinaForm
from .models import Professor

def discList(request):
    disc_list = Disciplina.objects.all()

    busca = request.GET.get('search')
    if busca:
        disc_list = Disciplina.objects.filter(nome__contains=busca)

    return render(request, 'disciplinas/discilist.html', {'disc_list': disc_list})

def discCad(request):
    prof = Professor.objects.all()
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sigla = form.cleaned_data['sigla']
            carga_hor = form.cleaned_data['carga_hor']
            semestre = form.cleaned_data['semestre']
            total_aulas = form.cleaned_data['total_aulas']
            aulas_semanais = form.cleaned_data['aulas_semanais']
            #status = form.cleaned_data['status']
            professor = form.cleaned_data['professor']
            categoria = form.cleaned_data['categoria']
            disciplina = form.save(commit=True)
            disciplina.save()
            
            return HttpResponseRedirect('/')
    else:
        form = DisciplinaForm
    return render(request, 'disciplinas/discicadastro.html', {'form': form, 'prof' : prof})

def deleteDisciplina(request, id):
    disciplina = get_object_or_404(Disciplina, pk=id)
    disciplina.delete()
    messages.info(request, 'Disciplina deletada com sucesso!')
    return redirect('/disciplinas/')

def editaDisciplina(request, id):
    disciplina = get_object_or_404(Disciplina, pk=id)
    form = DisciplinaForm(instance=disciplina)

    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)

        if form.is_valid():
            disciplina.save()
            return redirect('/')
        else:
            return render(request, 'disciplinas/editadisciplina.html', {'form': form, 'disciplina': disciplina})
        
    else:
        return render(request, 'disciplinas/editadisciplina.html', {'form': form, 'disciplina': disciplina})

def exibeDisciplina(request, id):
    disciplina = get_object_or_404(Disciplina, pk=id)
    return render(request, 'disciplinas/exibedisciplina.html', {'disciplina': disciplina})



