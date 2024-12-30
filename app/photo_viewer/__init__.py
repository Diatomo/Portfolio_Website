
from flask import Blueprint

bp = Blueprint('photo_viewer', __name__, url_prefix='/photoviewer')

def configure_login_manager(login_manager):
    login_manager.login_view = 'photo_viewer.login'

from app.photo_viewer import routes
