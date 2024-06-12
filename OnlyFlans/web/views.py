from django.shortcuts import render, redirect
from .models import Flan
from .models import ContactForm
from .forms import ContactFormModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def acerca(request):
    
    return render(request, 'about.html')


def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/')
    else:
        form = ContactFormModelForm()
    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'success.html')

def iniciar_sesion(request):
    error = False  # Inicializar la variable de error
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            error = True  # Establecer error a True si las credenciales son inválidas
    
    # Pasa el contexto con la variable de error a la plantilla
    return render(request, 'registration/login.html', {'error': error})
@login_required
def bienvenido(request):
    # Filtrar los flanes marcados como privados para el usuario autenticado
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados,
        'user': request.user 
    }
    return render(request, 'welcome.html', context)

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('index')