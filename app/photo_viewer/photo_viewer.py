

from app import app
from flask import session
from dotenv import load_dotenv
from flask_login import login_required, login_user, logout_user, UserMixin
import os

#FORM
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import os, time, math




'''
    LoginForm class

    Since this application is small and won't scale, I find it to be a bad idea to split
    apart the classes into too many files. I'll just keep whatever functionality is needed
    for the photo_viewer application all in one .py file.

'''

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Submit')


'''
    user class
'''
# User class
class User(UserMixin):
    def __init__(self, id):
        self.id = id


'''
    Class: PhotoViewer

    Login Class that is utilized to help keep some family photos
    safe from bots and unfriendly visitors. Maybe should be generalized
    to a login so I can utilize in other apps but may suffice in other
    family oriented applications I build in the future.

'''

class PhotoViewer:

    def __init__(self):
        self.FILETYPE = ".jpg"
        self.debug = False
        self.FAMILY_USERNAME = os.environ.get("FAMILY_USERNAME")
        self.FAMILY_PASSWORD = os.environ.get("FAMILY_PASSWORD")
        self.users = {self.FAMILY_USERNAME: {'password': self.FAMILY_PASSWORD}}
        self.lockout = False
        self.lockout_count = 0

    '''
        fxn: imageCheck

        Navigation check to see if we are downloading photos.
        Hardcoded to jpgs.

    '''
    def imageCheck(self, photos):

        result = True

        if (not photos):
            result = False

        for photo in photos:
            if (photo[-4:] !=  self.FILETYPE):
                result = False

        if self.debug:
            print("imageCheck status: " + str(result))

        return result


    '''
        fxn: getPhotos

        retrieves photos for a given path
    '''
    def getPhotos(self, path):

        if self.debug:
            print("fxn: family(path); PATH")
            print(path)

        root = "family_photos/"
        #path, specified by the request
        var_path = root + path + "/"
        if (root in path):
            var_path = path + "/"
        #full path to the photo files
        abs_path = os.path.join(app.static_folder, var_path)
        #collection of photo names
        photos = os.listdir(abs_path)

        if self.debug:
            print(path)
            print("photo name: " + photos[0])


        return {'var_path': var_path, 'photos': photos}

    '''
        fxn: userListExists

        Lockout check. Basically tying lockout to user. Primitive attempt to thwart
        someone trying to bruteforce their way in.

    '''
    def userListExists(self):

        try:
            if (not session['users']):
                session['users'] = []
        except:
            session['users'] = []


    '''
        fxn: clearSessionTimeouts

        Every 15 minutes the cache users[] should be cleared out.

    '''
    def clearSessionTimeouts(self, username):

        lockout_time = 15*60 #15 minutes
        self.userListExists()
        if (len(session['users']) > 0):
            for user in session['users']:
                if ((math.floor(time.time() - session[username]['creation_time'])) >= lockout_time):
                    session.pop(username, None)
                    session['users'].remove(username)


    def sessionPop(self, username):
        session.pop(username, None)

    '''
        fxn: lockoutCheck

        function responsible for locking out attempts on a specific username
    '''

    def lockoutCheck(self, username):

        if (username not in session):
            self.userListExists()
            if (len(session['users']) < 10): #Capping it so memory can't just be flooded again primitive but this is for a small < 5 people app.
                session['users'].append(username)
                session[username] = {'pw_attempts': 1, 'lockout': False, 'creation_time': time.time() }
            if self.debug:
                print(session[username])
        else:
            self.clearSessionTimeouts(username)
            if (session[username]['pw_attempts'] < 5):
                session[username]['pw_attempts'] += 1
                session.modified = True
            else:
                session[username]['lockout'] = True
        print (session)

        return session[username]['lockout']
