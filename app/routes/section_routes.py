from flask import Blueprint
from app.controllers.section_controller import get_sections, create_section

section_bp = Blueprint('section_bp', __name__)

section_bp.route('/sections', methods=['GET'])(get_sections)
section_bp.route('/sections', methods=['POST'])(create_section)
