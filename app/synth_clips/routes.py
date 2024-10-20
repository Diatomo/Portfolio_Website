
from flask import render_template
from . import bp

from app.logger import Logger
log = Logger()


@bp.route('/')
def clips():

    return render_template('apps/synth_clips/synthclips.html', title='Synth Clips')

