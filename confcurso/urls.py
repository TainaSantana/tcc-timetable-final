from django.urls import path
from .import views

app_name = 'confcurso'

urlpatterns = [
    path('cadastro/', views.restricaoCad, name='rest-cad'),
     
]