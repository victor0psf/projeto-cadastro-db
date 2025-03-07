#Second
from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request, 'users/home.html')

def users(request):
    #salvar os dados da tela para o banco
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()
    #exibir os users  cadastrados na tela
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retorna os resultados para pagina listagem de usuarios
    return render(request,'users/usuarios.html', usuarios)
    
