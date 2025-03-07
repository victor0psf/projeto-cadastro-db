#Fist 
from django.urls import path
from app_cadastro_users import views

urlpatterns = [
    #caminhos das minhas pags HTML
    path('', views.home, name='home'),
    path('users/', views.users, name='listagem_users')
]
