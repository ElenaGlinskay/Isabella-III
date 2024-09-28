from flask import Blueprint
from app.controllers.document_controller import get_documents, create_document

document_bp = Blueprint('document_bp', __name__)

document_bp.route('/documents', methods=['GET'])(get_documents)
document_bp.route('/documents', methods=['POST'])(create_document)
