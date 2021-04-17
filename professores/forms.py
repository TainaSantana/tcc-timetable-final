from django import forms

from .models import Professor

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ('nome', 'matricula', 'email', 'jornada_sem', 'max_aulas_dia')

