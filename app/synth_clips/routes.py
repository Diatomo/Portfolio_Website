
from flask import render_template
from .synth_clips import Synthclips
from . import bp



@bp.route('/')
def clips():

    baseurl = 'https://www.dropbox.com/home/Apps/diatomprojects-synthclips/'

    sc = Synthclips()
    sections = sc.format_sections()
    audioclips = sc.format_clips()

    return render_template('apps/synth_clips/synthclips.html', title='Synth Clips', dbxurl=baseurl, sections=sections, audioclips=audioclips)

