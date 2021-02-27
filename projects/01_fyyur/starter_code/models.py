from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer


db = SQLAlchemy()


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(12))
    genres = db.Column(db.ARRAY(db.String))
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String)
    
    #RELATIONSHIPS
    venue_shows = db.relationship('Show', backref='venue_shows', lazy=True)


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(12))
    genres = db.Column(db.ARRAY(db.String))
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String)

    #RELATIONSHIPS
    artist_shows = db.relationship('Show', backref='artist_shows', lazy=True)


class Show(db.Model):
    __tablename__ = 'show'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.TIMESTAMP(timezone=True))

    #FOREIGN KEYS
    venue_id = db.Column(
        db.Integer, 
        db.ForeignKey('venue.id'), 
        nullable=False)
    artist_id = db.Column(
        db.Integer,
        db.ForeignKey('artist.id'),
        nullable=False)

    #RELATIONSHIPS
    venue = db.relationship('Venue', backref='show_venue')
    artist = db.relationship('Artist', backref='show_artist')
