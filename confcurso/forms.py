from django import forms

class RestricaoForm(forms.Form):

    class Meta:
        #model = Restricao
        fields = ('semestre_atual', 'hora_inicio', 'hora_fim', 'dias_aula', 'n_geracoes', 'taxa_mutacao', 'status')