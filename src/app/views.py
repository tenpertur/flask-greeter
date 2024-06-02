from flask import Blueprint
from greet.infrastructure.rest import greet_bp

bp = Blueprint('main', __name__)

bp.register_blueprint(greet_bp)