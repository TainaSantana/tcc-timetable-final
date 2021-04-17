from django.urls import path
from .import views

app_name = 'algenetico'

urlpatterns = [
    path('', views.algGenetico, name='alg-genetico'),
    path('principal/', views.main, name='alg-main'),
]