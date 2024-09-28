from flask import jsonify, request
from app.models.document import Document
from app import mongo

doc_model = Document(mongo.db)

def get_documents():
    documents = list(doc_model.find_all_documents())
    return jsonify(documents), 200

def create_document():
    data = request.json
    doc_model.create_document(data)
    return jsonify({"message": "Documento creado exitosamente"}), 201
