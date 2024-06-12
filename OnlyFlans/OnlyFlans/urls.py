"""
URL configuration for OnlyFlans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web.views import indice, acerca, bienvenido
from web.views import contacto, exito
from web.views import iniciar_sesion, cerrar_sesion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name='index'),
    path('about/', acerca, name='about'),
    path('login/', iniciar_sesion, name='login'),
    path('welcome/', bienvenido, name='welcome'),
    path('logout/', cerrar_sesion, name='logout'),
    path('contact/', contacto, name='contact'),  # Nueva ruta para el formulario de contacto
    path('success/', exito, name='success'),  # Nueva ruta para la página de éxito
    path('accounts/', include('django.contrib.auth.urls')),  # Añadimos esta línea
    ]
