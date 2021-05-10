# Imports
#----------------------------------------------------------------------------#
from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

# TODO: connect to a local postgresql database
migration=Migrate(app,db)
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres=db.Column(db.String(120),nullable=False)
    website=db.Column(db.String(120))
    seeking_talent=db.Column(db.Boolean,default=False)
    seeking_description=db.Column(db.Text)
    past_shows_count=db.Column(db.Integer,default=0)
    upcoming_shows_count=db.Column(db.Integer,default=0)
    shows=db.relationship('Show',backref='venue',lazy='joined',cascade="save-update,merge,delete")


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website=db.Column(db.String(120))
    seeking_venue=db.Column(db.Boolean,default=False)
    seeking_description=db.Column(db.Text)
    past_shows_count=db.Column(db.Integer,default=0)
    upcoming_shows_count=db.Column(db.Integer,default=0)
    shows=db.relationship('Show',backref='artist',lazy='joined',cascade="save-update,merge,delete")


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__='Show'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    start_time = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer,db.ForeignKey('Artist.id')
                          ,nullable=False)
    venue_id = db.Column(db.Integer,db.ForeignKey('Venue.id')
                          ,nullable=False)
    upcoming = db.Column(db.Boolean, nullable=False, default=True)

#----------------------------------------------------------------------------#