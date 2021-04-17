from django.urls import path
from .import views

app_name = 'disciplinas'

urlpatterns = [
    path('cadastro/', views.discCad, name='disc-cad'),
    path('', views.discList, name='disc-list'),
    path('delete/<int:id>', views.deleteDisciplina, name='delete-disciplina'),
    path('exibedisciplina/<int:id>', views.exibeDisciplina, name='exibe-disciplina'),
    path('editadisciplina/<int:id>', views.editaDisciplina, name='edita-disciplina'),
]