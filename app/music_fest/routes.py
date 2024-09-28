
from flask import render_template
from .Music_fest import Musicfest
from . import bp


from app.logger import Logger
log = Logger()

@bp.route('/')
def psych_fest():

    msg = "A user has entered the music festival app."
    log.addEntry('info', msg)

    mf = Musicfest()
    title = 'psychfest24'
    video = mf.getVideo(title)
    audio = mf.getAudio(title)


    return render_template('apps/music_fest/music_fest.html', title='Music Festival', video=video, audio=audio)
