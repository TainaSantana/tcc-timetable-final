from django.db import models
#from disciplinas.models import Disciplina

class Professor(models.Model):

    STATUS_CHOICES = (
        ("1", "Ativo"),
        ("2", "Inativo"),
    ) 

    nome = models.CharField(max_length=150, blank=False, null=True)
    matricula = models.CharField(max_length=30, blank=False, null=False, unique=True)
    email = models.CharField(max_length=100)
    jornada_sem = models.IntegerField(blank=False)
    max_aulas_dia = models.IntegerField(blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, default=1)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
