
from flask import Blueprint

bp = Blueprint('photo_viewer', __name__, url_prefix='/photoviewer')

from app.photo_viewer import routes
