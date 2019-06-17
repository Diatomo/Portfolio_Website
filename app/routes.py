from flask import render_template, url_for, current_app
from app import app

@app.route('/')
@app.route('/index')
def index():
    projects = [
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
            "image" : "hexapod.jpg"
        },
        {
            "name" : 'Roto',
            "video" : 'https://www.youtube.com/watch?v=4urrSNMTg34',
            "code" : 'https://github.com/Diatomo/Roto_Private',
            'description' : 'Plan, design, build firm in which I built, designed, and programmed hardware systems for emergent interactives.',
            "endpoint" : "roto",
            "image" : "roto.png"
        },
        {
            "name" : 'TIAS',
            "video" : 'https://www.youtube.com/watch?v=p27bZ5V9P7E&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/School/tree/master/Tessellated-Information-Auditory-System',
            'description' : "Step Sequencer : With looping effects && layering multiple instruments. Try clicking on help on the top left  and clicking on a few squares.",
            "endpoint" : "tias",
            "image" : "tias.png"
        },
        {
            "name" : 'Gravity',
            "video" : 'https://www.youtube.com/watch?v=Ysz68Mc6vs8&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/Gravity',
            'description' : "Gravity Simulator : Emulates orbits of spawned planets around a sun",
            "endpoint" : "gravity",
            "image" : "gravity.png"
        },
        {
            "name" : 'Asteroids',
            "video" : 'https://www.youtube.com/watch?v=4o5iO1PYDYU&feature=youtu.be',
            "code" : 'http://www.codeskulptor.org/#user46_Yt9RESUGhC9ZCwm_3.py',
            'description' : 'Asteroids, one my first programs, with circle+cicle collisions and ammo',
            "endpoint" : "asteroids",
            "image" : "asteroids.png"
        },
        {
            "name" : 'Semi-Modular Patch Documentation',
            "video" : 'https://www.youtube.com/watch?v=X491o8rT-u4&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/Mother32_Preset',
            'description' : 'Moog Semimodular documentation for patching. Contains multiple moogs and a save feature',
            "endpoint" : "mother32",
            "image" : "mother32.png"
        },
        {
            "name" : 'Step Sequencer Hardware Prototype',
            "video" : 'https://www.youtube.com/watch?v=X491o8rT-u4&feature=youtu.be',
            "code" : 'https://github.com/Diatomo/Step-Sequencer',
            'description' : 'Designing and building a hardware step sequencer for a semi-moldular set',
            "endpoint" : "stepHW",
            "image" : "stepHW.jpg"
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
    return render_template('stepHW.html')

@app.route('/hexapod')
def hexapod():
    return render_template('hexapod.html')

@app.route('/otherworld')
def otherworld():
    return render_template('otherworld.html')

@app.route('/roto')
def roto():
    return render_template('roto.html')





