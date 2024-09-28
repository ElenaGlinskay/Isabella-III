# from flask import Flask
# from flask_pymongo import PyMongo
# from config.config import config

# app = Flask(__name__)
# app.config['SECRET_KEY'] = config.SECRET_KEY
# app.config['MONGO_URI'] = config.MONGO_URI

# mongo = PyMongo(app)

# from app.routes import document_routes, section_routes  # Importar rutas

# app.register_blueprint(document_routes.document_bp)
# app.register_blueprint(section_routes.section_bp)
# app/__init__.py
from flask import Flask
from flask_pymongo import PyMongo
from config.config import config
from .menu import obtener_menu, obtener_menu_privado


app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['MONGO_URI'] = config.MONGO_URI

mongo = PyMongo(app)

from app.routes import document_routes, section_routes  # Importar rutas

app.register_blueprint(document_routes.document_bp)
app.register_blueprint(section_routes.section_bp)

# Exportar las funciones de menú
def obtener_menu_publico():
    return obtener_menu()

def obtener_menu_privado_func():
    return obtener_menu_privado()
