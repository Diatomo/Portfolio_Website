
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_static_digest import FlaskStaticDigest


flask_static_digest = FlaskStaticDigest()

app = Flask(__name__)
flask_static_digest.init_app(app)



bootstrap = Bootstrap(app)
from app import routes
