from django.db import models
from professores.models import Professor

class Disciplina(models.Model):

    STATUS_CHOICES = (
        ("1", "Ativo"),
        ("2", "Inativo"),
    )

    CATEGORY_CHOICES = (
        ("1", "Teórica"),
        ("2", "Prática")
    )
    
    nome = models.CharField(max_length=150, blank=False, null=False)
    sigla = models.CharField(max_length=15, blank=False, null=False)
    carga_hor = models.IntegerField(blank=False, null=False)
    semestre = models.IntegerField(blank=False, null=False)
    total_aulas = models.IntegerField(blank=False, null=False)
    aulas_semanais = models.IntegerField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, default=1)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True) 
    atualizado_em = models.DateTimeField(auto_now=True)
    categoria = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    

    def __str__(self):
        return self.nome, self.professor, self.categoria
        #return self.professor






