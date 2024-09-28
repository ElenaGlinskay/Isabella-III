# app/app.py
from flask import render_template
from flask_login import login_required, current_user
from app import app
from app.menu import obtener_menu, obtener_menu_privado
from app.routes.auth import auth_bp  # Asegúrate de importar el Blueprint
# Variable de simulación para alternar entre layouts públicos y privados
es_layout_privado = False

# Crear un array de rutas
array_rutas = [
    {"nombre": "Inicio", "ruta": "/"},
    {"nombre": "Servicios", "ruta": "/services"},
    {"nombre": "Documentos", "ruta": "/documentos"},
    {"nombre": "Secciones", "ruta": "/secciones"},
    {"nombre": "Comunicados", "ruta": "/comunicados"},
    {"nombre": "Líderes", "ruta": "/lideres"},
    {"nombre": "Gerentes", "ruta": "/gerentes"},
    {"nombre": "Consultoras", "ruta": "/consultoras"},
    {"nombre": "Prospectos", "ruta": "/prospectos"},
    {"nombre": "Reincorporaciones", "ruta": "/reincorporaciones"},
    {"nombre": "Conferencias", "ruta": "/conferencias"},
    {"nombre": "Campañas", "ruta": "/campanas"},
    {"nombre": "Seguimientos", "ruta": "/seguimientos"},
]

def renderizar_con_layout_simulado(template, **context):
    layout = 'privade_layout.html' if es_layout_privado else 'public_layout.html'
    menu = obtener_menu_privado() if es_layout_privado else obtener_menu()
    return render_template(template, layout=layout, menu=menu, current_user=current_user, **context)

@app.route('/')
@login_required  # Asegúrate de que solo los usuarios autenticados accedan a esta ruta
def index():
    return renderizar_con_layout_simulado('index.html')  # Usamos la función para renderizar

@app.route('/otra-pagina')
@login_required  # Asegúrate de que esta ruta también requiera autenticación
def otra_pagina():
    return renderizar_con_layout_simulado('otra_pagina.html')

if __name__ == '__main__':
    app.run(debug=True)
