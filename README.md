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

## Estructura del proyecto
OnlyFlans/
  ├── OnlyFlans/
  │   ├── __pycache__/
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  ├── db.sqlite3
  ├── manage.py
  ├── requerimiento1/ 
  ├── requerimiento2/  
  ├── requerimiento3/  
  ├── vonlyflans/
  ├── onlyflans_mac.txt
  ├── OnlyFlans.png
  └── README.md

