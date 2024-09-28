from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from config.config import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['MONGO_URI'] = config.MONGO_URI

# Inicializa Flask-PyMongo
mongo = PyMongo(app)

# Configura Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Cambia 'login' por 'auth.login'

# Carga el usuario
@login_manager.user_loader
def load_user(user_id):
    # Cargar el usuario de la base de datos
    return mongo.db.users.find_one({"_id": user_id})  # Asegúrate de usar el método adecuado

# Importar y registrar blueprints
from app.routes import document_routes, section_routes, auth  # Cambia la orden de importación
app.register_blueprint(auth.auth_bp)  # Registra el Blueprint de autenticación
app.register_blueprint(document_routes.document_bp)
app.register_blueprint(section_routes.section_bp)

if __name__ == '__main__':
    app.run(debug=True)
