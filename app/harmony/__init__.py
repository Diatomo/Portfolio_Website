
from flask import Blueprint

bp = Blueprint('harmony', __name__, url_prefix='/harmony')

def configure_login_manager(login_manager):
    login_manager.login_view = 'harmony.login'

from app.harmony import routes
