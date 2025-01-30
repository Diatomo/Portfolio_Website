#app
from app import app, login_manager
from . import bp
#flask framework
from flask import request, after_this_request, jsonify,  flash, redirect, url_for, render_template
from flask_login import login_required, login_user, logout_user
#controller and implementation class
from .Harmony import HarmonyApp, LoginForm, User
from flask import session
#system
import os, time, math

from app.logger import Logger
log = Logger()


from dotenv import load_dotenv
load_dotenv()
MAX_ATTEMPTS = int(os.environ.get("MAX_LOGIN_ATTEMPTS"))

debug = False
cp = HarmonyApp()
root = 'harmony_app/'


@login_manager.user_loader
def load_user(user_id):
    if user_id in cp.users:
        return User(user_id)
    return None

@bp.route('/')
@login_required
def harmony_index():
    return render_template(root + 'index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    msg = "A user has entered the harmony app."
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
                if username in cp.users and cp.users[username]['password'] == password:
                    user = User(username)
                    login_user(user)
                    msg = "A user has successfully logged into the harmony app."
                    log.addEntry('info', msg)
                    session.pop('login_attempts', None)
                    session.pop('attempt_timestamp', None)
                    msg = "A user has successfully logged in."
                    log.addEntry('info', msg)
                    return redirect(url_for('harmony_app.harmony_index'))
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
    return redirect(url_for('harmony_app.login'))
