#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from datetime import datetime

import json
import dateutil.parser
import babel
import pytz
from flask import (
    Flask,
    render_template,
    request,
    Response,
    flash,
    redirect,
    url_for
)
from flask_moment import Moment
from flask_migrate import Migrate
from models import db, Venue, Artist, Show
from sqlalchemy.sql import func
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.dialects import postgresql
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from forms import ArtistForm, ShowForm, VenueForm
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
moment = Moment(app)
db.init_app(app)
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#


def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format)


app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def index():
    return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
    venues = Venue.query.all()
    venue_dict = {}
    data = []
    for venue in venues:
        num_show = sum([
            i.start_time > datetime.now(pytz.utc)
            for i in Venue.query.get(venue.id).venue_shows
        ])
        venue_final = {
            "id": venue.id,
            "name": venue.name,
            "num_upcoming_shows": num_show}
        dict_key = venue.city + '_' + venue.state
        if venue_dict.get(dict_key) is not None:
            venue_dict[dict_key].append(venue_final)
        else:
            venue_dict[dict_key] = [venue_final]
    for key in venue_dict.keys():
        data.append({
            "city": key.split('_')[0],
            "state": key.split('_')[1],
            "venues": venue_dict.get(key)
        })
    return render_template('pages/venues.html', areas=data)


@app.route('/venues/search', methods=['POST'])
def search_venues():
    search_term = request.form.get('search_term', '')
    venue_search = Venue.query.filter(
        Venue.name.ilike(
            '%{}%'.format(
                search_term.lower()))).all()
    data = []
    for venue in venue_search:
        data.append({"id": venue.id, "name": venue.name, "num_upcoming_shows": sum(
            [i.start_time > datetime.now(pytz.utc) for i in venue.venue_shows])})

    response = {"count": len(venue_search), "data": data}
    return render_template(
        'pages/search_venues.html',
        results=response,
        search_term=request.form.get(
            'search_term',
            ''))


@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
    venue_data = Venue.query.filter_by(id=venue_id).first_or_404()
    past_shows = db.session.query(Artist, Show).join(Show).join(Venue).filter(
        Show.venue_id == venue_id,
        Show.artist_id == Artist.id,
        Show.start_time < datetime.now()
    ).all()
    upcoming_shows = db.session.query(Artist, Show).join(Show).join(Venue).\
        filter(
        Show.venue_id == venue_id,
        Show.artist_id == Artist.id,
        Show.start_time > datetime.now()
    ).\
        all()
    data = {
        "id": venue_data.id,
        "name": venue_data.name,
        "genres": venue_data.genres,
        "address": venue_data.address,
        "city": venue_data.city,
        "state": venue_data.state,
        "phone": venue_data.phone,
        "website": venue_data.website,
        "facebook_link": venue_data.facebook_link,
        "seeking_talent": venue_data.seeking_talent,
        "seeking_description": venue_data.seeking_description,
        "image_link": venue_data.image_link,
        "past_shows": [{
            "artist_id": artist.id,
            "artist_name": artist.name,
            "artist_image_link": artist.image_link,
            "start_time": show.start_time.strftime("%m/%d/%Y, %H:%M")
        } for artist, show in past_shows],
        "upcoming_shows": [{
            "artist_id": artist.id,
            "artist_name": artist.name,
            "artist_image_link": artist.image_link,
            "start_time": show.start_time.strftime("%m/%d/%Y, %H:%M")
        } for artist, show in upcoming_shows],
        'past_shows_count': len(past_shows),
        'upcoming_shows_count': len(upcoming_shows)
    }
    return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------


@app.route('/venues/create', methods=['GET'])
def create_venue_form():
    form = VenueForm()
    return render_template('forms/new_venue.html', form=form)


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
    form = VenueForm(request.form)
    try:
        venue = Venue()
        form.populate_obj(venue)
        db.session.add(venue)
        venue.id = db.session.query(func.max(Venue.id)).first()[0] + 1
        db.session.commit()
        flash('Venue ' + request.form['name'] + ' was successfully listed!')
    except ValueError as e:
        print(e)
        flash(
            "An error occurred while trying to add new artist: {}".format(e),
            "error")
        db.session.rollback()
    finally:
        db.session.close()
    return render_template('pages/home.html')


@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    try:
        venue = Venue.query.get(venue_id)
        deleted_venue_name = venue.name
        db.session.delete(venue)
        db.session.commit()
        flash('{} was successfully deleted'.format(deleted_venue_name))
    except Exception as e:
        db.session.rollback()
        flash(
            "An error occurred while trying to delete {}: {}".format(
                venue_id, e), "error")
    finally:
        db.session.close()


#  Artists
#  ----------------------------------------------------------------


@app.route('/artists')
def artists():
    artists = Artist.query.with_entities(Artist.id, Artist.name).all()
    data = []
    for artist in artists:
        data.append({"id": artist.id, "name": artist.name})
    return render_template('pages/artists.html', artists=data)


@app.route('/artists/search', methods=['POST'])
def search_artists():
    search_term = request.form.get('search_term', '')
    artist_search = Artist.query.filter(
        Artist.name.ilike(
            '%{}%'.format(
                search_term.lower()))).all()
    data = []
    for artist in artist_search:
        data.append({"id": artist.id, "name": artist.name, "num_upcoming_shows": sum(
            [i.start_time > datetime.now(pytz.utc) for i in artist.artist_shows])})

    response = {"count": len(artist_search), "data": data}
    return render_template(
        'pages/search_artists.html',
        results=response,
        search_term=request.form.get(
            'search_term',
            ''))


@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
    artist_data = Artist.query.filter_by(id=artist_id).first_or_404()
    past_shows = db.session.query(Artist, Show).join(Show).join(Venue).filter(
        Show.artist_id == artist_id,
        Show.venue_id == Venue.id,
        Show.start_time < datetime.now()
    ).all()
    upcoming_shows = db.session.query(Show).join(Artist).join(Venue).filter(
        Show.artist_id == artist_id,
        Show.venue_id == Venue.id,
        Show.start_time > datetime.now()
    ).all()

    data = {
        "id": artist_data.id,
        "name": artist_data.name,
        "genres": artist_data.genres,
        "city": artist_data.city,
        "state": artist_data.state,
        "phone": artist_data.phone,
        "website": artist_data.website,
        "facebook_link": artist_data.facebook_link,
        "seeking_venue": artist_data.seeking_venue,
        "seeking_description": artist_data.seeking_description,
        "image_link": artist_data.image_link,
        "past_shows": [{
            "venue_id": venue.id,
            "venue_name": venue.name,
            "venue_image_link": venue.image_link,
            "start_time": show.start_time.strftime("%m/%d/%Y, %H:%M")
        } for venue, show in past_shows],
        "upcoming_shows": [{
            "venue_id": venue.id,
            "venue_name": venue.name,
            "venue_image_link": venue.image_link,
            "start_time": show.start_time.strftime("%m/%d/%Y, %H:%M")
        } for venue, show in upcoming_shows],
        'past_shows_count': len(past_shows),
        'upcoming_shows_count': len(upcoming_shows)
    }
    return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------


@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
    artist = Artist.query.first_or_404(artist_id)
    form = ArtistForm(obj=artist)
    return render_template('forms/edit_artist.html', form=form, artist=artist)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
    try:
        name = request.form.get('name')
        city = request.form.get('city')
        state = request.form.get('state')
        phone = request.form.get('phone')
        genres = request.form.getlist('genres')
        facebook_link = request.form.get('facebook_link')
        new_artists = Artist(
            name=name,
            city=city,
            state=state,
            phone=phone,
            genres=genres,
            facebook_link=facebook_link)
        db.session.add(new_artists)
        db.session.commit()

        flash('Artist ' + request.form['name'] + ' was successfully listed!')

    except Exception as e:
        db.session.rollback()

        flash(
            "An error occurred while trying to add new artist: {}".format(e),
            "error")
    finally:
        db.session.close()
    return redirect(url_for('show_artist', artist_id=artist_id))


@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
    venue = Venue.query.first_or_404(venue_id)
    form = VenueForm(obj=venue)
    return render_template('forms/edit_venue.html', form=form, venue=venue)


@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
    try:
        name = request.form.get('name')
        city = request.form.get('city')
        state = request.form.get('state')
        address = request.form.get('address')
        phone = request.form.get('phone')
        genres = request.form.getlist('genres')
        facebook_link = request.form.get('facebook_link')
        new_venues = Venue(
            name=name,
            city=city,
            state=state,
            address=address,
            phone=phone,
            genres=genres,
            facebook_link=facebook_link)
        db.session.add(new_venues)
        db.session.commit()

        flash('Venue ' + request.form['name'] + ' was successfully listed!')

    except Exception as e:
        db.session.rollback()

        flash(
            "An error occurred while trying to add new artist: {}".format(e),
            "error")
    finally:
        db.session.close()
    return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------


@app.route('/artists/create', methods=['GET'])
def create_artist_form():
    form = ArtistForm()
    return render_template('forms/new_artist.html', form=form)


@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
    form = ArtistForm(request.form)
    try:
        artist = Artist()
        form.populate_obj(artist)
        artist.id = db.session.query(func.max(Artist.id)).first()[0] + 1
        db.session.add(artist)
        db.session.commit()
        flash('Artist ' + request.form['name'] + ' was successfully listed!')
    except ValueError as e:
        print(e)
        flash(
            "An error occurred while trying to add new artist: {}".format(e),
            "error")
        db.session.rollback()
    finally:
        db.session.close()
    return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
    shows = Show.query.all()
    data = []
    for show in shows:
        data.append({"venue_id": show.venue_id,
                     "venue_name": show.venue.name,
                     "artist_id": show.artist_id,
                     "artist_name": show.artist.name,
                     "artist_image_link": show.artist.image_link,
                     "start_time": show.start_time.strftime("%Y-%m-%dT%X")})
    return render_template('pages/shows.html', shows=data)


@app.route('/shows/create')
def create_shows():
    form = ShowForm()
    return render_template('forms/new_show.html', form=form)


@app.route('/shows/create', methods=['POST'])
def create_show_submission():
    form = ShowForm(request.form)
    try:
        show = Show()
        form.populate_obj(show)
        show.id = db.session.query(func.max(Show.id)).first()[0] + 1
        db.session.add(show)
        db.session.commit()
        flash('Show was successfully listed!')
    except ValueError as e:
        flash("An error occurred. Show could not be listed. {}".format(e), "error")
        db.session.rollback()
    finally:
        db.session.close()
    return render_template('pages/home.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
