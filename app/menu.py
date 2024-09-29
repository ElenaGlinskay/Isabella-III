from flask import Flask, render_template, redirect, url_for, session
from flask_login import current_user

app = Flask(__name__)

def obtener_menu_privado():
    return [
        {
            "nombre": "Inicio",
            "ruta": "/",  # Ruta para la página de inicio
            "seccion": "presentation",
            "submenus": []
        },
        {
            "nombre": "Servicios",
            "submenus": [
                {"nombre": "Mostrar como Texto", "ruta": "/services/text", "formato": "text"},  # Ruta para el submenú
                {"nombre": "Mostrar como JSON", "ruta": "/services/json", "formato": "json"},
            ]
        },
        {
            "nombre": "Documentos",
            "submenus": [
                {"nombre": "Crear Documento", "ruta": "/documentos/create", "formato": "create"},
                {"nombre": "Listar Documentos", "ruta": "/documentos/list", "formato": "list"},
            ]
        },
        {
            "nombre": "Secciones",
            "submenus": [
                {"nombre": "Listar Secciones", "ruta": "/secciones/list", "formato": "list"},
            ]
        },
        {
            "nombre": "Comunicados",
            "submenus": [
                {"nombre": "Listar Comunicados", "ruta": "/comunicados/list", "formato": "list"},
            ]
        },
        {
            "nombre": "Líderes",
            "submenus": [
                {"nombre": "Listar Líderes", "ruta": "/lideres/list", "formato": "list"},
            ]
        },
        {
            "nombre": "Gerentes",
            "submenus": [
                {"nombre": "Listar Gerentes", "ruta": "/gerentes/list", "formato": "list"},
            ]
        },
        {
            "nombre": "Consultoras",
            "submenus": [
                {"nombre": "Listar Consultoras", "ruta": "/consultoras/list", "formato": "list"},
            ]
        },
        {
            "nombre": "Prospectos",
            "submenus": [
                {"nombre": "Listar Prospectos", "ruta": "/prospectos/list", "formato": "list"},
            ]
        },
        {
            "nombre": "Reincorporaciones",
            "submenus": [
                {"nombre": "Listar Reincorporaciones", "ruta": "/reincorporaciones/list", "formato": "list"},
            ]
        },
        {
            "nombre": "Conferencias",
            "submenus": [
                {"nombre": "Listar Conferencias", "ruta": "/conferencias/list", "formato": "list"},
            ]
        },
        {
            "nombre": "Campañas",
            "submenus": [
                {"nombre": "Listar Campañas", "ruta": "/campanas/list", "formato": "list"},
            ]
        },
        {
            "nombre": "Seguimientos",
            "submenus": [
                {"nombre": "Listar Seguimientos", "ruta": "/seguimientos/list", "formato": "list"},
            ]
        },
     
        {
            "nombre": "Cerrar Sesión",
            "ruta": "/logout",  # Ruta para cerrar sesión
            "submenus": []
        },
    ]

def obtener_menu():
    return [
        {
            "nombre": "Sobre Nosotros",
            "ruta": "/presentation",  # Ajustado para que sea un menú simple sin submenús
            "submenus": []
        },
        {
            "nombre": "Servicios",
            "submenus": [
                {"nombre": "Mostrar como Texto", "ruta": "/services/text", "formato": "text"},
                {"nombre": "Mostrar como JSON", "ruta": "/services/json", "formato": "json"},
            ]
        },
        {
            "nombre": "Iniciar Sesión",
            "ruta": "/login",  # Ruta para iniciar sesión
            "submenus": []
        },
        # Agrega más elementos según sea necesario
    ]

def esta_autenticado():
    return current_user.is_authenticated

def iniciar_sesion(user):
    session['user_id'] = user.id  # Almacena el ID del usuario en la sesión

def cerrar_sesion():
    session.pop('user_id', None)  # Elimina el ID del usuario de la sesión

if __name__ == '__main__':
    app.run(debug=True)


 