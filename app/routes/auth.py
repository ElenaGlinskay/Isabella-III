from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user
from app import mongo  # Asegúrate de que esta importación esté después de la declaración del Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({"username": username})  # Obtiene el usuario de la base de datos

        if user and user['password'] == password:  # Verifica la contraseña
            login_user(user)
            return redirect(url_for('index'))  # Redirige al índice

    return render_template('login.html')  # Asegúrate de que este archivo exista
