from django.db import models

class Restricoes(models.Model):

    SEMESTRE_CHOICES = (
        ("1", "1 Semestre"),
        ("2", "2 Semestre"),
    )

    """DIA_CHOICE(
        ("1", "Segunda"),
        ("2", "Terça"),
        ("3", "Quarta"),
        ("4", "Quinta"),
        ("5", "Sexta"),
        ("6", "Sábado"),
    )

    CHOICE_GERACAO(
        ("1", "50"),
        ("2", "75"),
        ("3", "100"),
    )

    STATUS_CHOICE(
        ("1", "Ativo"),
        ("2", "Inativo")
    )

    CHOICE_TAXA(
        ("1", "1.0"),
        ("2", "1.5"),
    )"""
    

    #periodo = models.CharField(max_length="1", choices=CHOICE_PERIOD, blank=False)
    semestre_atual = models.CharField(max_length=1, choices=SEMESTRE_CHOICES, null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True) # hora de inicio das aulas
    hora_fim = models.TimeField(null=True, blank=True) # hora de termino das aulas
    #dias_semana = models.IntegerField(max_length=1, choices=CHOICE_DIA) # dias da semana que as disciplinas serao ministradas
    #n_geracoes = models.IntegerField(max_length=1, choices=CHOICE_GERACAO)
    #taxa_mutacao = models.FloatField(max_length=1, choices=CHOICE_TAXA)
    #status = models.CharField(max_length=1, choices=CHOICE_STATUS)
    

