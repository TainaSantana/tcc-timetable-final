from django.db import models

class Sala(models.Model):

    LAB_CHOICES = (
        ("0", "Laboratório sem computadores"),
        ("1", "Laboratório com computadores"),
    )

    STATUS_CHOICES = (
        ("1", "Ativo"),
        ("2", "Inativo"),
    )

    nome = models.CharField(max_length=150, blank=False, null=False)
    bloco = models.CharField(max_length=2, blank=True)
    capacidade = models.CharField(max_length=4, blank=False, null=False)
    tipo_lab = models.CharField(max_length=1, choices=LAB_CHOICES, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, default=1)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
