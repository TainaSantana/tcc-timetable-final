from django.db import models

class Turma(models.Model):

    STATUS_CHOICES = (
        ("1", "Ativo"),
        ("2", "Inativo"),
    )

    nome = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, default=1)
    qtd_alunos = models.IntegerField(blank=False, null=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
 
