
from flask import Blueprint

bp = Blueprint('music_fest', __name__, url_prefix='/musicfest')

from app.music_fest import routes
