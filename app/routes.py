from flask import render_template, url_for, current_app
from app import app

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
@app.route('/index')
def index():
    projects = [
        {
            "name" : 'Modular Synthesizer',
            "video" : 'https://www.youtube.com/watch?v=JeMhOAyNEn0&ab_channel=MachineDreams',
            'description' : 'Machine built to sculpt music in an electric sandbox utilizing buttons, jacks and knobs',
            "endpoint" : "modular",
            "image" : "modular.jpg"
        },
        {
            "name" : 'Computer Generated Music',
            "code" : 'https://github.com/Diatomo/Generative_Music',
            'description' : 'Library of babel but for music',
            "endpoint" : "generative",
            "image" : "computer_generated_music.jpg"
        },
        {
            "name" : 'Otherworld - Unity',
            "video" : 'https://www.youtube.com/watch?v=TdyC8926eEo',
            "code" : 'https://github.com/Diatomo/Otherworld',
            'description' : 'Art Installation Company for interactive experiences. Built, designed and programmed Unity app, arduino scripts and applications on a raspberry pi with processing',
            "endpoint" : "otherworld",
            "image" : "otherworld.png"
        },
        {
            "name" : 'Hexapod Robot',
            "video" : 'https://www.youtube.com/watch?v=X491o8rT-u4&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/Hexapod',
            'description' : 'Building and Programming a Hexapod Robot :: Orignally Designed by Adammck',
            "endpoint" : "hexapod",
            "image" : "hexapod.jpg",
        },
        {
            "name" : 'Roto',
            "video" : 'https://www.youtube.com/watch?v=4urrSNMTg34',
            "code" : 'https://github.com/Diatomo/Roto_Private',
            'description' : 'Plan, design, build firm in which I built, designed, and programmed hardware systems for interactives.',
            "endpoint" : "roto",
            "image" : "roto.png",
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
            "name" : 'Semi-Modular Patch Documentation',
            "video" : 'https://www.youtube.com/watch?v=X491o8rT-u4&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/Mother32_Preset',
            'description' : 'Moog Semimodular documentation for patching. Contains multiple moogs and a save feature',
            "endpoint" : "mother32",
            "image" : "mother32.png",
        },
        {
            "name" : 'Step Sequencer Hardware Prototype',
            "video" : 'https://www.youtube.com/watch?v=X491o8rT-u4&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/Step-Sequencer',
            'description' : 'Designing and building a hardware step sequencer for a moldular set',
            "endpoint" : "stepHW",
            "image" : "stepHW.jpg",
        }
    ]
    return render_template('index.html', title='Home', projects=projects)


@app.route('/tias', methods=["GET", "POST"])
def tias():
    return current_app.send_static_file('tias.html')

@app.route('/gravity')
def gravity():
    return render_template('gravity.html')

@app.route('/mother32')
def mother():
    return render_template('mother32.html')

@app.route('/stepHW')
def stepHW():
    title = "Step Sequencer Hardware"
    description = '''The step-sequencer hardware system originally started as a school project. 
    It was nothing particularly new, however; played an important role in analog/digital modular sound synthesis.
    It was a natural path on learning more about customand open source hardware. It also introduced Charles to 
    developing electronics hardware from scratch using professional tools such as Eagle.'''
    projects = [ 
        {
            "name" : "Prototype",
            "image" : 'step_prototype.jpg',
            "post" : "Protype begin on breadboards with hundreds of wires and a few cans of beer.",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Button Board",
            "image" : 'step_button.jpg',
            "post" : "With shortcomings of a prototyped breadboard, a new board was brought to life. Which utilized neopixels and a flashy pcb laceur",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Multiplexer",
            "image" : 'step_multiplexer.jpg',
            "post" : "Modularity was key to create a system that could be expanded thus the multiplexer drove the input of the button board",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Software",
            "image" : 'step_software.png',
            "post" : "To control everything a small Object Oriented C++ program was created utilizing the arduino compiler for a teensy board along with the platformIO framework",
            "code" : None,
            "video" : None
        }
    ]
    return render_template('project.html', title=title, description=description, projects=projects)

@app.route('/hexapod')
def hexapod():
    title = "Hexapod"
    description = '''Hexapod built to began designing a kinematic system for robots 
    but eventually test reinforcment learning algorithms as well as computer vision.'''
    projects =[
        {
            "name" : "Prototype",
            "image" : 'hexapod_prototype.jpg',
            "post" : "Hexapod Robot built with pulse width modulated servo motors.",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Assembly",
            "image" : 'hexapod_assembly.jpg',
            "post" : "Parts collection before assembly. Included legs, feet, a body, smart servo motors, and a raspberry pi",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Software",
            "image" : 'hexapod_software.png',
            "post" : '''Designed in a layered object oriented archetecture following the mathematics and research for Hexapod Functionality. 
                      This includes, servo api, legs, head, pose, gait, hexapod state machine, and an input controller.''',
            "code" : "https://github.com/Diatomo/Hexapod",
            "video" : None
        }
    ]
    return render_template('project.html', title=title, description=description, projects=projects)

@app.route('/otherworld')
def otherworld():
    title = "Otherworld"
    description = '''
            Otherworld was a small company that designed and built interactive art spaces. 
            They built rooms and hallways filled with escape room and haunted house elements. 
            This included enigmatic puzzles, fantastical sculpture, audio, and textiles
            as well as interactive projection mapping and otherworldy led animations. The technologist
            position thus required tenacity as well as innovative problem solving.'''
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
    ]
    return render_template('project.html', title=title, description=description, projects=projects)

@app.route('/roto')
def roto():
    title = "Roto"
    description = ''' Roto was a plan, design and build firm for the immersive  
            interactive entertainment industry. They catered toward 
            children's science and art museums. Exhibit Engineers designed 
            and implemented the electrical and programming elements of each exhibit.'''
    projects = [
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



@app.route('/modular')
def modular():
    title = "Modular"
    description = ''' Modular Dummy Text '''
    projects = [
        {
            "name" : "Music",
            "image" : 'modular.jpg',
            "post" : "Modular Dummy Text",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Schematics",
            "image" : 'modular.jpg',
            "post" : "Modular Dummy Text",
            "code" : None,
            "video" : None
        }
    ] 
    return render_template('project.html', title=title, description=description, projects=projects)


@app.route('/generative')
def generative():
    title = "Computer Generated Music"
    description = ''' Generated music Dummy Text '''
    projects = [
        {
            "name" : "Music",
            "image" : 'computer_generated_music.jpg',
            "post" : "Computer Generated Music Dummy Text",
            "code" : None,
            "video" : None
        },
        {
            "name" : "Schematics",
            "image" : 'computer_generated_music.jpg',
            "post" : "Computer Generated Music Dummy Text",
            "code" : None,
            "video" : None
        }
    ] 
    return render_template('project.html', title=title, description=description, projects=projects)

