

import os
from pydub import AudioSegment
from app import app

class Musicfest:

    def __init__(self):
        self.directory_path = os.path.join(app.static_folder, 'music_fest')
        self.content = os.listdir(self.directory_path)

    def getVideo(self, title):
        result = ''
        form = 'mp4'
        for video in self.content:
            if form in video:
                if title in video:
                    result = video
        return(result)

    def getAudio(self, title):
        result = ''
        form = 'wav'
        for audio in self.content:
            if form in audio:
                if title in audio:
                    result = audio
        return(result)

