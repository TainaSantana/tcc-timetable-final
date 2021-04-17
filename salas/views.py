from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import SalaForm
from .models import Sala

 

def salaList(request):

    salas_list = Sala.objects.all()

    busca = request.GET.get('search')
    if busca:
        salas_list = Sala.objects.filter(nome__contains=busca)

    return render(request, 'salas/salalist.html', {'salas_list': salas_list})

def exibeSala(request, id):
    sala = get_object_or_404(Sala, pk=id)
    return render(request, 'salas/exibesala.html', {'sala': sala})

def salaCad(request):
  
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            bloco = form.cleaned_data['bloco']
            capacidade = form.cleaned_data['capacidade'] 
            tipo_lab = form.cleaned_data['tipo_lab']
            #status = form.cleaned_data['status']
            sala = form.save(commit=True)
            sala.save()
            return HttpResponseRedirect('/')
    else:
        form = SalaForm
    return render(request, 'salas/salacadastro.html', {'form': form})

def deleteSala(request, id):
    sala = get_object_or_404(Sala, pk=id)
    sala.delete()
    messages.info(request, 'Sala deletada com sucesso!')
    return redirect('/salas/')


def editaSala(request, id):
    sala = get_object_or_404(Sala, pk=id)
    form = SalaForm(instance=sala)

    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)

        if form.is_valid():
            sala.save()
            return redirect('/')
        else:
            return render(request, 'salas/editasala.html', {'form': form, 'sala': sala})
        
    else:
        return render(request, 'salas/editasala.html', {'form': form, 'sala': sala})



