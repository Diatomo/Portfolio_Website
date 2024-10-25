#app
from app import app, login_manager
from . import bp
#flask framework
from flask import request, after_this_request, jsonify,  flash, redirect, url_for, render_template
from flask_login import login_required, login_user, logout_user
#controller and implementation class
from .photo_viewer import PhotoViewer, LoginForm, User
from flask import session
#system
import os, time, math

from app.logger import Logger
log = Logger()


from dotenv import load_dotenv
load_dotenv()
MAX_ATTEMPTS = int(os.environ.get("MAX_LOGIN_ATTEMPTS"))
UPLOAD_PATH = os.environ.get("PVP_PATH")

debug = False
pv = PhotoViewer()
root = 'photo_viewer/'


def formatLog():
    dt = datetime.datetime.now()
    result = str(dt) + ': '
    return result

@login_manager.user_loader
def load_user(user_id):
    if user_id in pv.users:
        return User(user_id)
    return None

@bp.route('/<path:path>/photo', methods=['GET'])
@login_required
def photo(path):

    result = pv.getPhotos(path)
    photos = result['photos']
    var_path = result['var_path']
    title = var_path.split('/')
    if len(title) == 3:
        title = title[-2] + ' ' + 'Events'
    elif len(title) == 4:
        title = title[-3] + ' ' + title[-2]
    else:
        title = var_path

    if (pv.imageCheck(photos)):
        return render_template(root + 'photo.html', photos=photos, endpoint=var_path, title=title, demo=False)
    else:
        return render_template(root + 'photo_menu.html', dirs=photos, title=title, tag=var_path)


@bp.route('/')
@login_required
def menu():
    title = "Year"
    directory_path = os.path.join(app.static_folder, 'family_photos')
    dirs = os.listdir(directory_path)
    return render_template(root + 'photo_menu.html', dirs=dirs, title=title, tag=None)


@bp.route('/upload')
@login_required
def upload():
    title = "Upload Photos"
    return render_template(root + 'upload.html', title=title)

@bp.route('/demo_upload')
def demo_upload():
    title = "Demo Upload Photos"
    return render_template(root + 'demo_upload.html', title=title)

@bp.route('/upload_files', methods=['GET', 'POST'])
def upload_files():

    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    if 'files[]' not in request.files:
        return jsonify({"error": "No files part"}), 400

    files = request.files.getlist('files[]')

    if not files:
        return jsonify({"error": "No files selected"}), 400

    file_paths = []
    for file in files:
        if file.filename == '':
            return jsonify({"error": "One of the files has no name"}), 400


        file_path = os.path.join(UPLOAD_PATH, file.filename)
        file.save(file_path)
        file_paths.append(file_path)

    time.sleep(2)
    return jsonify({"message": "Files successfully uploaded", "files": file_paths}), 200


@bp.route('/demo_upload_files', methods=['GET', 'POST'])
def demo_upload_files():
    time.sleep(2)
    return jsonify({"message": "Files successfully uploaded", "files": file_paths}), 200



@bp.route('/demo')
def demo():
    title = "Demo"
    directory_path = os.path.join(app.static_folder, 'images')
    endpoint = directory_path.split('/')
    endpoint = endpoint[-1]
    photos = os.listdir(directory_path)
    return render_template(root + 'photo.html', photos=photos, endpoint=endpoint, title=title, demo=True)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    msg = "A user has entered the photo viewer."
    log.addEntry('info', msg)
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            if ('login_attempt' not in session):
                session.setdefault('login_attempts', 0)
                session.setdefault('attempt_timestamp', time.time())
            elif ('attempt_timestamp' in session and time.time() - session('attempt_timestamp') / (15*60) >= 1):
                session['login_attempts'] = 0
                session['attempt_timestamp'] = time.time()

            if (session['login_attempts'] <= MAX_ATTEMPTS):
                if username in pv.users and pv.users[username]['password'] == password:
                    user = User(username)
                    login_user(user)
                    msg = "A user has successfully logged into the photo viewer."
                    log.addEntry('info', msg)
                    session.pop('login_attempts', None)
                    session.pop('attempt_timestamp', None)
                    directory_path = os.path.join(app.static_folder, 'family_photos')
                    photos = os.listdir(directory_path)
                    msg = "A user has successfully logged in."
                    log.addEntry('info', msg)
                    return redirect(url_for('photo_viewer.menu'))
                else:
                    session['login_attempts'] += 1
                    session['attempt_timestamp'] = time.time()
                    error = "Invalid username or password. Please try again."
            else:
                error = 'Account Locked. Please try again later.'

    return render_template(root + 'login.html', form=form, error=error)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('photo_viewer.login'))
