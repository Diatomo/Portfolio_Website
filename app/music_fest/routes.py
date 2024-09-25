
from flask import render_template
from .Music_fest import Musicfest
from . import bp



@bp.route('/')
def psych_fest():

    mf = Musicfest()
    title = 'psychfest24'
    video = mf.getVideo(title)
    audio = mf.getAudio(title)


    return render_template('apps/music_fest/music_fest.html', title='Music Festival', video=video, audio=audio)
