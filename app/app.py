from flask import render_template
from app import app
from app.menu import obtener_menu, obtener_menu_privado  # Asegúrate de importar correctamente

es_layout_privado = False  # Cambia a True para simular el layout privado

def renderizar_con_layout_simulado(template, **context):
    """
    Renderiza usando el layout público o privado, según la simulación.
    """
    menu = obtener_menu_privado() if es_layout_privado else obtener_menu()  # Simula el menú según el layout

    return render_template(template, layout='public_layout.html', menu=menu, **context)

# @app.route('/')
# def index():
#     return renderizar_con_layout_simulado('index.html')

# @app.route('/otra-pagina')
# def otra_pagina():
#     return renderizar_con_layout_simulado('otra_pagina.html')

if __name__ == '__main__':
    app.run(debug=True)
