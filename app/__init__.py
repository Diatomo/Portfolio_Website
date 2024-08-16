
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_static_digest import FlaskStaticDigest
from flask_minify import minify
from flask_login import LoginManager
from datetime import timedelta

flask_static_digest = FlaskStaticDigest()

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)
flask_static_digest.init_app(app)
minify(app=app, html=True, js=True, cssless=True)

bootstrap = Bootstrap(app)
from app import routes
