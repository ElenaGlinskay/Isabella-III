from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

mongo = PyMongo()
bcrypt = Bcrypt()

def create_user(username, password):
    # Hashea la contraseña
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    mongo.db.users.insert_one({'username': username, 'password': hashed_password})

def find_user(username):
    return mongo.db.users.find_one({'username': username})

def check_password(hashed_password, password):
    return bcrypt.check_password_hash(hashed_password, password)
