from django.urls import path
from .import views

app_name = 'professores'

urlpatterns = [
    path('cadastro/', views.profCad, name='prof-cad'),
    path('', views.profList, name='prof-list'),
    path('delete/<int:id>', views.deleteProf, name='delete-prof'),
    path('exibeprof/<int:id>', views.exibeProf, name='exibe-prof'),
    path('editaprof/<int:id>', views.editaProf, name='edita-prof'),
]