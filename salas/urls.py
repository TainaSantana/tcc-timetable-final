from django.urls import path
from .import views


app_name = 'salas'

urlpatterns = [
    path('cadastro/', views.salaCad, name='sala-cad'),
    path('', views.salaList, name='sala-list'),
    path('delete/<int:id>', views.deleteSala, name='delete-sala'),
    path('exibesala/<int:id>', views.exibeSala, name='exibe-sala'),
    path('editasala/<int:id>', views.editaSala, name='edita-sala'),
    
]