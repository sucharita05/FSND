from datetime import datetime
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL, Regexp


STATES = [
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('DC', 'DC'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
]

GENRES = [
    ('Alternative', 'Alternative'),
    ('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Funk', 'Funk'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Heavy Metal', 'Heavy Metal'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Musical Theatre', 'Musical Theatre'),
    ('Pop', 'Pop'),
    ('Punk', 'Punk'),
    ('R&B', 'R&B'),
    ('Reggae', 'Reggae'),
    ('Rock n Roll', 'Rock n Roll'),
    ('Soul', 'Soul'),
    ('Other', 'Other'),
]


class ShowForm(Form):
    artist_id = StringField('Artist ID', validators=[DataRequired()]
    )
    venue_id = StringField('Venue ID', validators=[DataRequired()]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=STATES
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone', validators=[
                            Regexp(r'\d{10}',
                                   message='Phone number must be in format 123-456-7890')]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=GENRES      
    )
    website = StringField(
        'Website', validators=[URL(message='Website link is not a valid URL')]
    )
    image_link = StringField(
        'image_link', validators=[URL(message='Image link is not a valid URL')]
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(message='Facebook link is not a valid URL')]
    )
    seeking_talent = BooleanField(
        'Seeking Talent'
    )
    seeking_description = StringField(
        'Seeking Talent Description'
    )

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=STATES
    )
    phone = StringField(
        'phone', validators=[
                            Regexp(r'\d{10}',
                                   message='Phone number must be in format 123-456-7890')]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=GENRES      
    )
    website = StringField(
        'Website', validators=[URL(message='Website link is not a valid URL')]
    )
    image_link = StringField(
        'image_link', validators=[URL(message='Image link is not a valid URL')]
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(message='Facebook link is not a valid URL')]
    )
    seeking_venue = BooleanField(
        'Seeking Venue'
    )
    seeking_description = StringField(
        'Seeking Venue Description'
    )
