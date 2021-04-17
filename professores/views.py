from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Professor
from .forms import ProfessorForm
from disciplinas.models import Disciplina

def profList(request):
    prof_list = Professor.objects.all()
    disc_list = Disciplina.objects.all()

    busca = request.GET.get('search')
    if busca:
        prof_list = Professor.objects.filter(nome__contains= busca)
    return render(request, 'professores/proflist.html', {'prof_list': prof_list, 'disc_list': disc_list})

def profCad(request):
    #disc_list = Disciplina.objects.all()

    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            matricula = form.cleaned_data['matricula']
            email = form.cleaned_data['email']
            jornada_sem = form.cleaned_data['jornada_sem']
            max_aulas_dia = form.cleaned_data['max_aulas_dia']
            #status = form.cleaned_data['status']
            professor = form.save(commit=True)
            professor.save()
            return HttpResponseRedirect('/')
    else:
        form = ProfessorForm
    return render(request, 'professores/profcadastro.html', {'form': form})

def deleteProf(request, id):
    professor = get_object_or_404(Professor, pk=id)
    professor.delete()
    messages.info(request, 'Professor deletado com sucesso!')
    return redirect('/professores/')

def editaProf(request, id):
    professor = get_object_or_404(Professor, pk=id)
    form = ProfessorForm(instance=professor)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)

        if form.is_valid():
            professor.save()
            return redirect('/')
        else:
            return render(request, 'professores/editaprof.html', {'form': form, 'professor': professor})
        
    else:
        return render(request, 'professores/editaprof.html', {'form': form, 'professor': professor})

def exibeProf(request, id):
    professor = get_object_or_404(Professor, pk=id)
    return render(request, 'professores/exibeprof.html', {'professor': professor})