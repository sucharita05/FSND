import os
from flask import Flask, request, abort, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Actor, Movie


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
            'success': True
        }), 200

  
  # Actors
  #-------------------------------------

    @app.route('/actors', methods=['GET'])
    def get_actor():
        actors = Actor.query.all()
        print(actors)
        actor_list = []
        for actor in actors:
            actor_list.append(
                {"name": actor.name, "age": actor.age, "gender": actor.gender})

        if len(actors) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'actors': actor_list,
            'total_actors': len(actors)
        }), 200

    @app.route('/actors/add', methods=['POST'])
    def add_actors():
      try:
        data = request.get_json()
        if data is None:
            abort(404)
        new_name = data.get('name')
        new_age = data.get('age')
        new_gender = data.get('gender')

        # Validate to ensure no data is empty
        if (len(new_name) == 0 or new_age == 0 or len(new_gender) == 0):
            abort(400)
        # Create a new actor instance
        new_actors = Actor(
            name=new_name,
            age=new_age,
            gender=new_gender
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
      except Exception:
          abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    def update_actors(actor_id):
      data = request.get_json()

      try:
        update_actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        # Abort 404 if there is no actor to update
        if update_actor is None:
            abort(404)
        # Assign the data to update actor name
        update_actor.name = data.get('name', update_actor.name)
        # Assign the data to update actor age
        update_actor.age = data.get('age', update_actor.age)
        # Assign the data to update actor gender
        update_actor.gender = data.get('gender', update_actor.gender)
        # Update the actor
        update_actor.update()

        # Return a success message
        return jsonify({
            'success': True
        }), 200
      except Exception:
          abort(400)


    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    def delete_actors(actor_id):
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

      except Exception:
        abort(404)


  
    # Movies
    #--------------------------------------

    @app.route('/movies', methods=['GET'])
    def get_movie():
        movies = Movie.query.all()
        data = []
        for movie in movies:
            data.append({"title": movie.title,
                         "release_date": movie.release_date})

        if len(movies) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'movies': data,
            'total_movies': len(movies)
        }), 200

    @app.route('/movies/add', methods=['POST'])
    def add_movies():
      try:
        data = request.get_json()

        if data is None:
            abort(404)
        new_title = data.get('title')
        new_release_date = data.get('release_date')

        # Validate to ensure no data is empty
        if (len(new_title) == 0 or new_release_date == 0):
            abort(400)
        # Create a new movie instance
        new_movies = Movie(
            title=new_title,
            release_date=new_release_date
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

      except Exception:
          abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    def update_movies(movie_id):
      data = request.get_json()

      try:
        update_movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        # Abort 404 if there is no movie to update
        if update_movie is None:
            abort(404)
        # Assign the data to update movie title
        update_movie.title = data.get('title', update_movie.title)
        # Assign the data to update movie release date
        update_movie.release_date = data.get('release_date', update_movie.release_date)
        
        # Update the movie
        update_movie.update()

        # Return a success message
        return jsonify({
            'success': True
        }), 200

      except Exception:
          abort(400)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movies(movie_id):
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

      except Exception:
        abort(404)

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


    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
