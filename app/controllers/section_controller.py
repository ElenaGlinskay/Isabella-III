from flask import jsonify, request
from app.models.section import Section
from app import mongo

section_model = Section(mongo.db)

def get_sections():
    sections = list(section_model.find_all_sections())
    return jsonify(sections), 200

def create_section():
    data = request.json
    section_model.create_section(data)
    return jsonify({"message": "Sección creada exitosamente"}), 201
