
from flask import render_template
from .synth_clips import Synthclips
from . import bp

from app.logger import Logger
log = Logger()


@bp.route('/')
def clips():

    msg = "A user has entered the synth clips app."
    log.addEntry('info', msg)

    baseurl = 'https://www.dropbox.com/home/Apps/diatomprojects-synthclips/'

    sc = Synthclips()
    sections = sc.format_sections()
    audioclips = sc.format_clips()

    return render_template('apps/synth_clips/synthclips.html', title='Synth Clips', dbxurl=baseurl, sections=sections, audioclips=audioclips)

