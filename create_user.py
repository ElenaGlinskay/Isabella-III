from werkzeug.security import generate_password_hash
from app import mongo

# Crear una nueva contraseña hasheada utilizando el método predeterminado
hashed_password = generate_password_hash("testpassword")  # No es necesario especificar 'method'

# Guardar el usuario en la base de datos
mongo.db.users.insert_one({
    "username": "testuser",
    "password": hashed_password
})

print("Usuario agregado con contraseña hasheada.")
