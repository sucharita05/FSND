import os
from datetime import datetime
from flask import Flask, request, abort, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import jose

from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/', methods=['GET'])
    def get_home():
        return jsonify({
            'message': 'Welcome to Star in Making',
            'success': True
        }), 200

    @app.route('/about', methods=['GET'])
    def get_about():
        return jsonify({
            'message': 'A Professional Casting Agency',
            'success': True
        }), 200

  # Actors
  # -------------------------------------

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actor(token):
        actors = Actor.query.order_by(Actor.first_name).all()
        actor_list = []
        for actor in actors:
            actor_list.append({"id": actor.id,
                               "first_name": actor.first_name,
                               "last_name": actor.last_name,
                               "age": actor.age,
                               "gender": actor.gender,
                               "image_link": actor.image_link})

        if len(actors) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'actors': actor_list,
            'total_actors': len(actors)
        }), 200

    @app.route('/actors/add', methods=['POST'])
    @requires_auth('post:actors')
    def add_actors(token):
        try:
            data = request.get_json()
            if data is None:
                abort(404)
            new_first_name = data.get('first_name')
            new_last_name = data.get('last_name')
            new_age = data.get('age')
            new_gender = data.get('gender')
            new_image_link = data.get('image_link')

            # Validate to ensure no data is empty
            if (len(new_first_name) == 0 or len(new_last_name) == 0 or new_age == 0 or len(new_gender) == 0):
                abort(400)
            # Create a new actor instance
            new_actors = Actor(
                first_name=new_first_name,
                last_name=new_last_name,
                age=new_age,
                gender=new_gender,
                image_link=new_image_link
            )
            # Insert the actor to the database
            new_actors.insert()
            # Get all actors
            new_actors = Actor.query.order_by(Actor.id).all()
            current_actor = [actor.format() for actor in new_actors]

            # Return a success message
            return jsonify({
                'success': True,
                'actors': current_actor,
                'total_actors': len(new_actors)
            }), 200
        except BaseException:
            abort(400)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actors(payload, actor_id):
        data = request.get_json()

        try:
            update_actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()
            # Abort 404 if there is no actor to update
            if update_actor is None:
                abort(404)
            # Assign the data to update actor first name
            update_actor.first_name = data.get(
                'first_name', update_actor.first_name)
            # Assign the data to update actor last name
            update_actor.last_name = data.get(
                'last_name', update_actor.last_name)
            # Assign the data to update actor age
            update_actor.age = data.get('age', update_actor.age)
            # Assign the data to update actor gender
            update_actor.gender = data.get('gender', update_actor.gender)
            # Assign the data to update actor image
            update_actor.image_link = data.get(
                'image_link', update_actor.image_link)
            # Update the actor
            update_actor.update()

            # Return a success message
            return jsonify({
                'success': True
            }), 200
        except BaseException:
            abort(400)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(payload, actor_id):
        try:
            # Get the actors by id
            actor = Actor.query.filter(
                Actor.id == actor_id).one_or_none()

            # Abort 404 if no actors found
            if actor is None:
                abort(404)
            # Else, delete the actor
            actor.delete()
            # Return a success message
            return jsonify({
                'success': True,
                'deleted': actor_id
            }), 200

        except BaseException:
            abort(422)

    # Movies
    # --------------------------------------

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movie(token):
        movies = Movie.query.all()
        recent_movies = Movie.query.order_by(Movie.release_date).filter(
            Movie.release_date <= datetime.now()).all()
        upcoming_movies = Movie.query.order_by(Movie.release_date).filter(
            Movie.release_date > datetime.now()).all()
        recent_movies_data = []
        upcoming_movies_data = []
        for movie in recent_movies:
            recent_movies_data.append({"id": movie.id,
                                       "title": movie.title,
                                       "release_date": movie.release_date,
                                       "image_link": movie.image_link
                                       })
        for movie in upcoming_movies:
            upcoming_movies_data.append({"id": movie.id,
                                        "title": movie.title,
                                         "release_date": movie.release_date,
                                         "image_link": movie.image_link
                                         })

        if len(movies) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'recent_movies': recent_movies_data,
            'upcoming_movies': upcoming_movies_data,
            'total_movies': len(movies),
            'recent_movies_count': len(recent_movies),
            'upcoming_movies_count': len(upcoming_movies)
        }), 200

    @app.route('/movies/add', methods=['POST'])
    @requires_auth('post:movies')
    def add_movies(token):
        try:
            data = request.get_json()

            if data is None:
                abort(404)
            new_title = data.get('title')
            new_release_date = data.get('release_date')
            new_image_link = data.get('image_link')

            # Validate to ensure no data is empty
            if (len(new_title) == 0 or new_release_date == 0):
                abort(400)
            # Create a new movie instance
            new_movies = Movie(
                title=new_title,
                release_date=new_release_date,
                image_link=new_image_link
            )
            # Insert the movie to the database
            new_movies.insert()
            # Get all movies
            new_movies = Movie.query.order_by(Movie.id).all()
            current_movies = [movie.format() for movie in new_movies]

            # Return a success message
            return jsonify({
                'success': True,
                'movies': current_movies,
                'total_movies': len(new_movies)
            }), 200

        except BaseException:
            abort(400)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movies(payload, movie_id):
        data = request.get_json()

        try:
            update_movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()
            # Abort 404 if there is no movie to update
            if update_movie is None:
                abort(404)
            # Assign the data to update movie title
            update_movie.title = data.get('title', update_movie.title)
            # Assign the data to update movie release date
            update_movie.release_date = data.get(
                'release_date', update_movie.release_date)
            # Assign the data to update movie image
            update_movie.image_link = data.get(
                'image_link', update_movie.image_link)

            # Update the movie
            update_movie.update()

            # Return a success message
            return jsonify({
                'success': True
            }), 200

        except BaseException:
            abort(400)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(payload, movie_id):
        try:
            # Get the movies by id
            movie = Movie.query.filter(
                Movie.id == movie_id).one_or_none()

            # Abort 404 if no movies found
            if movie is None:
                abort(404)
            # Else, delete the movie
            movie.delete()
            # Return a success message
            return jsonify({
                'success': True,
                'deleted': movie_id
            }), 200

        except BaseException:
            abort(422)

    @app.route('/contact', methods=['GET'])
    def get_contact():
        return jsonify({
            'message': 'Contact Us',
            'success': True
        }), 200

    # Create error handlers for all expected errors
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unproceessable entity'
        }), 422

     # Create auth error handlers

    @app.errorhandler(401)
    def page_not_found(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400


    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "forbidden"
        }), 403

    return app


# APP = create_app()

# if __name__ == '__main__':
#     APP.run(host='0.0.0.0', port=8080, debug=True)
