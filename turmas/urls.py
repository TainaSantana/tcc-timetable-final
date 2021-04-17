from django.urls import path
from .import views

app_name = 'turmas'

urlpatterns = [
    path('cadastro/', views.turmaCad, name='turma-cad'),
    path('', views.turmaList, name='turma-list'),
    path('delete/<int:id>', views.deleteTurma, name='delete-turma'),
    path('exibeturma/<int:id>', views.exibeTurma, name='exibe-turma'),
    path('editaturma/<int:id>', views.editaTurma, name='edita-turma'),
]