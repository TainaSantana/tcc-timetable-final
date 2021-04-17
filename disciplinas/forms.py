from django import forms

from .models import Disciplina


class DisciplinaForm(forms.ModelForm):

    class Meta:
        model = Disciplina
        fields = ('nome', 'sigla', 'carga_hor', 'semestre', 'total_aulas', 'aulas_semanais', 'professor', 'categoria')


