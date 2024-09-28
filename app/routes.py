from flask import render_template, url_for, current_app, jsonify
from flask import send_from_directory
from flask import session
from flask import request
from dotenv import load_dotenv
from app import app, login_manager
from .logger import Logger
import time
import math
import os
import io
import datetime

from pydub import AudioSegment

from flask_login import login_required, login_user, logout_user, UserMixin

log = Logger()

load_dotenv()
app.secret_key = os.environ.get("SECRET_KEY")
debug = False

# Route to serve the JSON file
@app.route('/assets/particles.json')
def serve_particles():
    return send_from_directory('assets', 'particles.json')

@app.route('/')
def index():
    msg = "A user has entered the diatom projects website."
    log.addEntry('info', msg)
    projects = [
        {
            "name": 'Music Festival',
            "video": '',
            "code": '',
            "description": "Music festival ambient performance and visual.",
            "endpoint": "/musicfest",
            "image": "music_fest.jpg"

        },
        {
            "name": 'Photo Viewer',
            "video": '',
            "code": '',
            "description": "Dropbox media repository viewer. Meant for family members only. Demo is available at bottom of login page.",
            "endpoint": "/photoviewer",
            "image": "photo_viewer.jpg"
        },
        {
            "name": 'Tri VCO',
            "video": '',
            "code": '',
            "description": 'Triple Voltage Controlled Oscillator build for a modular synthesizer.',
            "endpoint": "trivco",
            "image": "osc_prototype_oscilloscope.jpg"
        }
    ]

    oldprojects = [
        {
            "name": 'Synth Clips',
            "video": '',
            "code": '',
            "description": 'Synth club audio clips.',
            "endpoint": "/clips",
            "image": "synth_clips.jpg"
        },
        {
            "name" : 'TIAS',
            "video" : 'https://www.youtube.com/watch?v=p27bZ5V9P7E&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/School/tree/master/Tessellated-Information-Auditory-System',
            'description' : "Step Sequencer : With looping effects && layering multiple instruments. Try clicking on help on the top left and clicking on a few squares.",
            "endpoint" : "old_tias",
            "image" : "tias.png"
        },
        {
            "name" : 'Gravity',
            "video" : 'https://www.youtube.com/watch?v=Ysz68Mc6vs8&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/Gravity',
            'description' : "Gravity Simulator : Emulates orbits of spawned planets around a sun, click around and watch the little planets orbit.",
            "endpoint" : "old_gravity",
            "image" : "gravity.png"
        },
        {
            "name" : 'Asteroids',
            "video" : 'https://www.youtube.com/watch?v=4o5iO1PYDYU&feature=youtu.be',
            "code" : 'https://py2.codeskulptor.org/#user49_GFkrajcmPH_1.py',
            'description' : 'Asteroids, one my first programs, with circle to cicle collisions and ammo',
            "endpoint" : "asteroids",
            "image" : "asteroids.png"
        },
        {
            "name" : "School Projects",
            "image" : 'study.jpg',
            "description" : "Collection of work that I wrote through my undergraduate program, including A.I., datamining, and bioinformatics projects.",
            "code" : 'https://github.com/Inkozi/School',
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Infinity Hall",
            "image" : 'otherworld_infinity.jpg',
            "description" : "Distorted the space around you with mirrors and leds. Space is not what one perceives it to be but rather a fabric that bends around you.",
            "code" : '',
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Sleeper Pods",
            "image" : "otherworld_sleeper.jpg",
            "description" : "When one interacts with the pods it beams your soul through soul sucking led animations",
            "code" : '',
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Funeral Scene",
            "image" : 'otherworld_funeral.jpg',
            "description" : "Brought the boundary of life and death together by soaking the color out of the room but when triggered would bring them back to life.",
            "code" : "https://github.com/Diatomo/Otherworld/tree/master/Funeral_Scene/Funeral_Scene",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Unity Display Case",
            "image" : 'otherworld_unity.jpg',
            "description" : "A narrative display case with Unity that illustrates the corruption and maddening nature of Otherworld's experiments.",
            "code" : '',
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Kelp Forest",
            "image" : 'otherworld_kelp.jpg',
            "description" : "Center-Peice of otherworld, in which a tree with glowing orbs illuminates mystery and wonder.",
            "code" : "https://github.com/Diatomo/Otherworld/blob/master/Seaweed/Seaweed.ino",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "The Watcher",
            "image" : 'otherworld_watcher.jpg',
            "description" : "A beast with many eyes watches you as you traverse beneath them, they say that when one stares into the abyss it stares back into you.",
            "code" : '',
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Command Center",
            "image" : 'otherworld_command.jpg',
            "description" : "Command and watch the rooms at Otherworld Industries. Buttons interact with led animation across the exhibit space and Otherworld's internal documentation is exposed.",
            "code" : '',
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Stalagtites",
            "image" : 'otherworld_stalagtites.jpg',
            "description" : "Magical stalagtites offer an interactive that play musical harmonies when a hand is swept between them.",
            "code" : '',
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Blanket Fort",
            "image" : 'otherworld_blanket.jpg',
            "description" : "Relax, although reality is crumbling around you, a little cove of alien plant life shimmers as one may enjoy its alien beauty.",
            "code" : "https://github.com/Diatomo/Otherworld/blob/master/Blanket_Fort/Blanket_Fort.ino",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Glow Lab",
            "image" : 'otherworld_glowlab.jpg',
            "description" : "A laboratory of alien life is being experimented on and harvested.",
            "code" : '',
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "MD-80 Display Case",
            "image" : 'roto_md80.png',
            "description" : "This exhibit allowed one to experience and learn about the complexity of flying an MD80 with a dynamic display.",
            "code" : "https://github.com/Diatomo/Roto_Private/blob/master/COMPLETE/CRSMITH/MD80/MD80.ino",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Luggage Stack",
            "image" : 'roto_luggage.png',
            "description" : "Race against time to see if you're better than a professional. This was a game where kids and grownups had to stack luggage for a potential flight.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/COMPLETE/CRSMITH/Luggage_Stack_CCS_NEW/Luggage_Stack_CCS.ino",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "People of American Airlines",
            "image" : 'roto_people.png',
            "description" : "Diversity is key when it comes to running an airline. This exhibit allowed employees to discuss who they were and how they contributed to such a large service.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/COMPLETE/CRSMITH/Story_Corps/Story_Corps.ino",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "The Ohio State Constitution",
            "image" : 'roto_constitution.jpg',
            "description" : "First ever live display case of the authentic Ohio state consitution.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/OHIO_STATEHOUSE/OhioConstitution/OhioConstitution.ino",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Noodle Forest",
            "image" : 'roto_noodle.jpg',
            "description" : "A jungle gym for children to run through boxing bags triggering lidar controlled crystalline sounds.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/COMPLETE/HIGH_MUSEUM/Noodle_Forest/Noodle_Forest.ino",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Whisper Tube",
            "image" : 'roto_tube.jpg',
            "description" : "Whisper your message into a microphone and the message would trasnmit via a rasperry pi led animation.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/tree/master/Acrylic_Tube",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Cycle to Power",
            "image" : 'roto_cycle.jpg',
            "description" : "Bike your way to beat the clock converting mechanical energy into electrical energy. Then watch your progress as appliances animate with the energy one created.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/tree/master/Cycle_To_Power_MotherBox/src",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Sound Vibration",
            "image" : 'roto_sound.jpg',
            "description" : "Ever wonder what sound looks like? In this exhibit, individuals could see the sound waves with sand placed upon a vibrating plate.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/COMPLETE/FRIST/Sound_Vibration/Sound_Vibration.ino",
            "video" : '',
            "endpoint" : ''
        },
        {
            "name" : "Knox Cube",
            "image" : 'roto_knox.png',
            "description" : "Test your memory with this simon says game. A test for immigrants coming to America.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/COMPLETE/AKRON/Knox_Prototype/Knox_Prototype.ino",
            "video" : '',
            "endpoint" : ''
        }
    ]

    projects = projects + oldprojects
    return render_template('index.html', title='Diatom-Projects', projects=projects)


@app.route('/trivco')
def trivco():
    title = "Triple Voltage Controlled Oscillator"
    description = "Project to learn about hardware electronics, triple voltage controlled oscillator for modular synthesizer."

    directory_path = os.path.join(app.static_folder, 'trivco_audio')
    audioclips = os.listdir(directory_path)

    result = []

    for clip in audioclips:
        temp = {}
        if (clip == 'trivco_raw_processed.wav'):
            temp['label'] = 'raw oscillator'
        else:
            temp['label'] = 'reverb oscillator'
        temp['audio'] = clip

        audio = AudioSegment.from_file(directory_path + '/' + clip)
        duration_ms = len(audio)
        duration_seconds = duration_ms // 1000
        minutes = duration_seconds // 60
        seconds = duration_seconds % 60

        if (len(str(seconds)) <= 1):
            seconds = str(seconds) + '0'
        temp['length'] = str(minutes) + ':' + str(seconds)

        result.append(temp)

    return render_template('trivco.html', title=title, audioclips=result)


#==========================================================================
'''
    OLD ROUTES

    progress is halted on these projects. I think I have hit a point in
    my career where I need to create better quality applications. I will
    keep everything here for completion and something to look back on.
'''
#==========================================================================



@app.route('/old_tias', methods=["GET", "POST"])
def tias():
    return current_app.send_static_file('processing/tias.html')

@app.route('/old_gravity')
def gravity():
    return render_template('legacy/gravity.html')

@app.route('/old_about')
def about():
    title = "About"
    info = {
        "name" : "about",
        "image" : 'profile_picture.jpg',
    }
    return render_template('oldprojects/about.html', title=title, info=info)

