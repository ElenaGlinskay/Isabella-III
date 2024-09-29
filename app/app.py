# app/app.py
from flask import render_template
from flask_login import login_required, current_user
from app import app
from app.menu import obtener_menu, obtener_menu_privado
from app.routes.auth import auth_bp  # Asegúrate de importar el Blueprint
# Variable de simulación para alternar entre layouts públicos y privados
es_layout_privado = False


def renderizar_con_layout_simulado(template, **context):
    layout = 'layouts/privade_layout.html' if es_layout_privado else 'layouts/public_layout.html'
    menu = obtener_menu_privado() if es_layout_privado else obtener_menu()
    return render_template(template, layout=layout, menu=menu, current_user=current_user, **context)

@app.route('/')

def index():
    return renderizar_con_layout_simulado('index.html')  # Usamos la función para renderizar



if __name__ == '__main__':
    app.run(debug=True)
