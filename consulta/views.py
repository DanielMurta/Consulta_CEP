from django.shortcuts import render

# Renderizando a Página Inicial
def home(request):
    return render(request, 'home.html')

