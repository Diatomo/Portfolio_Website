
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


bootstrap = Bootstrap(app)
from app import routes, models
