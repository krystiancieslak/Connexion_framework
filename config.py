import pathlib
import pytz
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# create timezone object for Poland
poland_tz = pytz.timezone("Europe/Warsaw")

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__)
app = connex_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)