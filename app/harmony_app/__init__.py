
from flask import Blueprint

bp = Blueprint('harmony_app', __name__, url_prefix='/harmony-app')

def configure_login_manager(login_manager):
    login_manager.login_view = 'harmony_app.login'

from app.harmony_app import routes
