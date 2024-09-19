
from flask import Blueprint

bp = Blueprint('synth_clips', __name__, url_prefix='/clips')

from app.synth_clips import routes
