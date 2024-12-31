

from app import app
from flask import session
from dotenv import load_dotenv
from flask_login import login_required, login_user, logout_user, UserMixin
import os

#FORM
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import os, time, math

load_dotenv()


'''
    LoginForm class

    Since this application is small and won't scale, I find it to be a bad idea to split
    apart the classes into too many files. I'll just keep whatever functionality is needed
    for the harmony application all in one .py file.

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
    Class: Harmony

    Data Member class for some security protecting a development prototype.

'''

class HarmonyApp:

    def __init__(self):
        self.debug = False
        self.MEMBER_USERNAME = os.environ.get("MEMBER_USERNAME")
        self.MEMBER_PASSWORD = os.environ.get("MEMBER_PASSWORD")
        self.users = {self.MEMBER_USERNAME: {'password': self.MEMBER_PASSWORD}}
        self.lockout = False
        self.lockout_count = 0

