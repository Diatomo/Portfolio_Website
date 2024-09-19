#app
from app import app, login_manager
from . import bp
#flask framework
from flask import request, flash, redirect, url_for, render_template
from flask_login import login_required, login_user, logout_user
#controller and implementation class
from .photo_viewer import PhotoViewer, LoginForm, User
#system
import os, time, math

debug = False
pv = PhotoViewer()
root = 'apps/photo_viewer/'


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

    if (pv.imageCheck(photos)):
        return render_template(root + 'photo.html', photos=photos, endpoint=var_path, title=var_path, demo=False)
    else:
        return render_template(root + 'photo_menu.html', dirs=photos, title=var_path, tag=var_path)


@bp.route('/')
@login_required
def menu():
    title = "Menu"
    directory_path = os.path.join(app.static_folder, 'family_photos')
    dirs = os.listdir(directory_path)
    return render_template(root + 'photo_menu.html', dirs=dirs, title=title, tag=None)


@bp.route('/demo')
def demo():
    title = "images"
    directory_path = os.path.join(app.static_folder, title)
    endpoint = directory_path.split('/')
    endpoint = endpoint[-1]
    photos = os.listdir(directory_path)
    return render_template(root + 'photo.html', photos=photos, endpoint=endpoint, title=title, demo=True)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if (not pv.lockoutCheck(username)):
                if username in pv.users and pv.users[username]['password'] == password:
                    pv.sessionPop(username)
                    user = User(username)
                    login_user(user)
                    directory_path = os.path.join(app.static_folder, 'family_photos')
                    photos = os.listdir(directory_path)
                    return redirect(url_for('photo_viewer.menu'))
                else:
                    return redirect(url_for('photo_viewer.login'))
            else:
                error = 'Username is Locked out, Please try again later.'

    return render_template(root + 'login.html', form=form, error=error)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('photo_viewer.login'))
