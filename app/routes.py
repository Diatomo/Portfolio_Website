from flask import render_template, url_for, current_app
from app import app

@app.route('/')
@app.route('/index')
def index():
    projects = [
        {
            "name" : 'HGRIC',
            "video" : '',
            "code" : '',
            'description' : 'Bioinformatics core maintaing and developing a consortium research database.',
            "endpoint" : "hgric",
            "image" : "bioinformatics.jpg"
        },
        {
            "name" : 'TIAS',
            "video" : 'https://www.youtube.com/watch?v=p27bZ5V9P7E&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/School/tree/master/Tessellated-Information-Auditory-System',
            'description' : "Step Sequencer : With looping effects && layering multiple instruments. Try clicking on help on the top left and clicking on a few squares.",
            "endpoint" : "tias",
            "image" : "tias.png"
        },
        {
            "name" : 'Gravity',
            "video" : 'https://www.youtube.com/watch?v=Ysz68Mc6vs8&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/Gravity',
            'description' : "Gravity Simulator : Emulates orbits of spawned planets around a sun, click around and watch the little planets orbit.",
            "endpoint" : "gravity",
            "image" : "gravity.png"
        },
        {
            "name" : 'Asteroids',
            "video" : 'https://www.youtube.com/watch?v=4o5iO1PYDYU&feature=youtu.be',
            "code" : 'http://www.codeskulptor.org/#user46_Yt9RESUGhC9ZCwm_3.py',
            'description' : 'Asteroids, one my first programs, with circle to cicle collisions and ammo',
            "endpoint" : "asteroids",
            "image" : "asteroids.png"
        },
        {
            "name" : 'Patch Documentation - Incomplete',
            "video" : 'https://www.youtube.com/watch?v=X491o8rT-u4&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/Mother32_Preset',
            'description' : 'Moog Semimodular documentation application for patching. When I first was learning how to play a synthesizer, I often find myself creating some interesting sounds but forgetting how I made them. I decided to create a program to help me save and record patches.',
            "endpoint" : "mother32",
            "image" : "mother32.png",
        }
    ]
    return render_template('index.html', title='Home', projects=projects)

@app.route('/exhibits')
def exhibits():
    title = "Art Installations"
    description = '''
        Art installations built, designed, and installed over two years from Texas to Ohio, including a display case
        for the real Ohio constitution.
        '''
    projects =  [
        {
            "name" : "Infinity Hall",
            "image" : 'otherworld_infinity.jpg',
            "post" : "Distorted the space around you with mirrors and leds. Space is not what one perceives it to be but rather a fabric that bends around you.",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Sleeper Pods",
            "image" : "otherworld_sleeper.jpg",
            "post" : "When one interacts with the pods it beams your soul through soul sucking led animations", 
            "code" : None,
            "video" : None
        },
        {
            "name" : "Funeral Scene",
            "image" : 'otherworld_funeral.jpg',
            "post" : "Brought the boundary of life and death together by soaking the color out of the room but when triggered would bring them back to life.",
            "code" : "https://github.com/Diatomo/Otherworld/tree/master/Funeral_Scene/Funeral_Scene",
            "video" : None
        },
        {
            "name" : "Unity Display Case",
            "image" : 'otherworld_unity.jpg',
            "post" : "A narrative display case with Unity that illustrates the corruption and maddening nature of Otherworld's experiments.",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Kelp Forest",
            "image" : 'otherworld_kelp.jpg',
            "post" : "Center-Peice of otherworld, in which a tree with glowing orbs illuminates mystery and wonder.",
            "code" : "https://github.com/Diatomo/Otherworld/blob/master/Seaweed/Seaweed.ino",
            "video" : None
        },
        {
            "name" : "The Watcher",
            "image" : 'otherworld_watcher.jpg',
            "post" : "A beast with many eyes watches you as you traverse beneath them, they say that when one stares into the abyss it stares back into you.",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Command Center",
            "image" : 'otherworld_command.jpg',
            "post" : "Command and watch the rooms at Otherworld Industries. Buttons interact with led animation across the exhibit space and Otherworld's internal documentation is exposed.",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Stalagtites",
            "image" : 'otherworld_stalagtites.jpg',
            "post" : "Magical stalagtites offer an interactive that play musical harmonies when a hand is swept between them.",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Blanket Fort",
            "image" : 'otherworld_blanket.jpg',
            "post" : "Relax, although reality is crumbling around you, a little cove of alien plant life shimmers as one may enjoy its alien beauty.",
            "code" : "https://github.com/Diatomo/Otherworld/blob/master/Blanket_Fort/Blanket_Fort.ino",
            "video" : None
        },
        {
            "name" : "Glow Lab",
            "image" : 'otherworld_glowlab.jpg',
            "post" : "A laboratory of alien life is being experimented on and harvested.",
            "code" : None,
            "video" : None
        },
        {
            "name" : "MD-80 Display Case",
            "image" : 'roto_md80.png',
            "post" : "This exhibit allowed one to experience and learn about the complexity of flying an MD80 with a dynamic display.",
            "code" : "https://github.com/Diatomo/Roto_Private/blob/master/COMPLETE/CRSMITH/MD80/MD80.ino",
            "video" : None
        },
        {
            "name" : "Luggage Stack",
            "image" : 'roto_luggage.png',
            "post" : "Race against time to see if you're better than a professional. This was a game where kids and grownups had to stack luggage for a potential flight.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/COMPLETE/CRSMITH/Luggage_Stack_CCS_NEW/Luggage_Stack_CCS.ino",
            "video" : None
        },
        {
            "name" : "People of American Airlines",
            "image" : 'roto_people.png',
            "post" : "Diversity is key when it comes to running an airline. This exhibit allowed employees to discuss who they were and how they contributed to such a large service.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/COMPLETE/CRSMITH/Story_Corps/Story_Corps.ino",
            "video" : None
        },
        {
            "name" : "The Ohio State Constitution Display",
            "image" : 'roto_constitution.jpg',
            "post" : "First ever live display case of the authentic Ohio state consitution.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/OHIO_STATEHOUSE/OhioConstitution/OhioConstitution.ino",
            "video" : None
        },
        {
            "name" : "Noodle Forest",
            "image" : 'roto_noodle.jpg',
            "post" : "A jungle gym for children to run through boxing bags triggering lidar controlled crystalline sounds.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/COMPLETE/HIGH_MUSEUM/Noodle_Forest/Noodle_Forest.ino",
            "video" : None
        },
        {
            "name" : "Whisper Tube",
            "image" : 'roto_tube.jpg',
            "post" : "Whisper your message into a microphone and the message would trasnmit via a rasperry pi led animation.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/tree/master/Acrylic_Tube",
            "video" : None
        },
        {
            "name" : "Cycle to Power",
            "image" : 'roto_cycle.jpg',
            "post" : "Bike your way to beat the clock converting mechanical energy into electrical energy. Then watch your progress as appliances animate with the energy one created.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/tree/master/Cycle_To_Power_MotherBox/src",
            "video" : None
        },
        {
            "name" : "Sound Vibration",
            "image" : 'roto_sound.jpg',
            "post" : "Ever wonder what sound looks like? In this exhibit, individuals could see the sound waves with sand placed upon a vibrating plate.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/COMPLETE/FRIST/Sound_Vibration/Sound_Vibration.ino",
            "video" : None
        },
        {
            "name" : "Knox Cube",
            "image" : 'roto_knox.png',
            "post" : "Test your memory with this simon says game. A test for immigrants coming to America.",
            "code" : "https://github.com/Diatomo/Roto-Arduino-Scripts/blob/master/COMPLETE/AKRON/Knox_Prototype/Knox_Prototype.ino",
            "video" : None
        }
    ]
    return render_template('project.html', title=title, description=description, projects=projects)


@app.route('/tias', methods=["GET", "POST"])
def tias():
    return current_app.send_static_file('tias.html')

@app.route('/gravity')
def gravity():
    return render_template('gravity.html')

@app.route('/mother32')
def mother():
    return render_template('mother32.html')

@app.route('/music')
def music():
    title = "Music"
    description = ''' Music '''
    projects = [
        {
            "name" : "Dark Portal",
            "image" : 'dark_portal.png',
            "post" : "Dark Portal Summoning Spirits.",
            "music" : "https://www.dropbox.com/s/c15pwe9ibzpics4/Late_Night_Portal.mp4?dl=0"
        },
        {
            "name" : "Ambient_001",
            "image" : 'ambient_001.png',
            "post" : "Ambient 001",
            "music" : "https://www.dropbox.com/s/freczmem7fk6kl2/AMBIENT%20001.mp4?dl=0"
        },
        {
            "name" : "Ambient_002",
            "image" : 'ambient_002.png',
            "post" : "Ambient 002",
            "music" : "https://www.dropbox.com/s/ynhztbddnpki1ol/ambient_002.mp4?dl=0"
        },
        {
            "name" : "October Track",
            "image" : 'october.png',
            "post" : "October Track",
            "music" : "https://www.dropbox.com/s/fpvs72uqposn1pc/Instagram_10.11.2021.mp4?dl=0"
        }

    ]
    return render_template('music.html', title=title, description=description, projects=projects)


'''
@app.route('/hgric')
def hgric():
    title = "Human Genetic Research Informatics Core"
    description = "Bioinformatics research lab seeking the genetic causes of Dilated Cardiomyopathy (DCM)"
    return render_template('hgric.html', title=title, description=description)
'''
