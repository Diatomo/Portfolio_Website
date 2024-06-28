
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_static_digest import FlaskStaticDigest
from flask_minify import minify

flask_static_digest = FlaskStaticDigest()

app = Flask(__name__)
flask_static_digest.init_app(app)
minify(app=app, html=True, js=True, cssless=True)



bootstrap = Bootstrap(app)
from app import routes
