# HITO 1 
# OnlyFlans
# paso a paso utilizado para MAC

![OnlyFlans Logo](./OnlyFlans.png)

OnlyFlans es un proyecto de Django. Este README proporciona una guía paso a paso para configurar el entorno y poner en marcha el proyecto OnlyFlans en mi máquina local.

## Creación de Entorno Virtual

1. Crear un entorno virtual:
   bash
   ```python3 -m venv vOnlyFlans```
2. Activar el entorno virtual:
   ```source vOnlyFlans/bin/activate```
3. Instalar Django: 
   ```pip3 install Django==5.0.6```
4. Guardar las dependencias instaladas:    
   ```pip3 freeze > requirements-vOnlyflans.txt```
5. verificar la version de python: (salir con ctrl + d)  
   ```python3 --version``` (3.12.2)

## Creación de Proyecto
1. Crear un proyecto Django:
   ```django-admin startproject OnlyFlans```
2. Navegar al directorio del proyecto:   
   ```cd OnlyFlans```
3. Crear migraciones: 
   ```python3 manage.py makemigrations```
4. Aplicar migraciones:
   ```python3 manage.py migrate```
5. Ejecutar el servidor de desarrollo: 
   ```python3 manage.py runserver``` (detener ctrl + c)

__________________________________________________________________

# HITO 2 

## Entrar al entorno virtual y activarlo
    source vOnlyFlans/bin/activate

# Creacion de aplicacion web 

1. crear aplicacion web:
   ```python3 manage.py startapp web```
2. agregar la aplicacion web a "setting.py"
   ```web```
3. crear la carpeta "templates"   
   ```dentro de la app web crear una carpeta llamada "templates"```
4. crear el archivo "index.html"
   ```dentro de "web/templates" crear un archivo llamado "index.html"```
5. crear el archivo "about.html"   
   ```dentro de "web/templates" crear un archivo llamado "about.html"```
6. crear el archivo "welcome.html"
   ```dentro de "web/templates" crear un archivo llamado "welcome.html"```
7. configurar las vistas y la URLs
   
 a. views.py:
   def index(request):
       return render(request, 'index.html')
   def about(request):
       return render(request, 'about.html')
   def welcome(request):
      return render(request, 'welcome.html')

      
 b. urls.py:
   from web.views import index, about, welcome  

   urlpatterns = [
    path('', index, 'index'),
    path('about/', about, 'about'),
    path('welcome/', welcome, 'welcome'),
]    

8. ejecutrar el servidor de desarollo 
   ```python3 manage.py runserver```

   navegar las rutas about y welcome
