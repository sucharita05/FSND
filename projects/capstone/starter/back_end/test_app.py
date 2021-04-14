import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie

#This class represents the capstone test case
class CapstoneTestCase(unittest.TestCase):
    
    #Define test variables and initialize app.
    def setUp(self):
        
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres','postgres','localhost:5432', self.database_name)
    
        # binds the app to the current context
        setup_db(self.app, self.database_path)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    #Executed after reach test  
    def tearDown(self):
        pass
    
    def test_get_home(self):
        response = self.client().get('/')
        # Check the status code and message
        self.assertEqual(response.status_code, 200)

    def test_get_about(self):
        response = self.client().get('/')
        # Check the status code and message
        self.assertEqual(response.status_code, 200)

    def test_get_actors(self):
        # Make the request and process the response
        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        # Check for the total_actors and that the actors return data
        self.assertTrue(data['total_actors'])
        self.assertTrue(len(data['actors']))
    
    # Tests that an actor can be created and is successful
    def test_post_new_actors(self):
        # Create variable for mock data to use as payload for post request
        self.new_actor = {
            "name": "Test Actor Name",
            "age": 30,
            "gender": "Test Gender",
            "image_link": "Test Image_ink"
        }
        # Creates the new actor and loads the response data
        response = self.client().post('/actors/add', json=self.new_actor)
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        # Check for the created actor, total_actors and that the
        # actors return data
        self.assertTrue(data['total_actors'])
        self.assertTrue(len(data['actors']))

    # Tests that  when a actor is not created, an appropriate error
    # response is delivered
    def test_400_if_actor_does_not_create(self):
        # Create variable for mock actor data to use as payload for failed
        # add request
        self.new_actor = {
            "name": "",
            "age": 29,
            "gender": "Male",
            "image_link": "https://www.google.com/"
        }
        # make request and process response
        response = self.client().post('/actors/add', json=self.new_actor)
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    def test_update_actor_age(self):
        # Updates the actor and loads the response data
        response = self.client().patch('/actors/21', json={'age': 28})
        data = json.loads(response.data)
        # Get the actor from the database
        actor = Actor.query.filter(Actor.id == 21).one_or_none()

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.format()['age'], 28)

    # Tests that when an actor is not updated, an appropriate error
    # response is delivered
    def test_400_actor_for_failed_update(self):
        # Update variable for mock actor data to use as payload for failed
        # patch request
        # make request and process response
        response = self.client().patch('/actors/21')
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    # Tests that  when a actor is deleted and is successful that it returns
    # appropriate response
    def test_delete_actor(self):
        # Delete the actor and process response
        response = self.client().delete('/actors/19')
        data = json.loads(response.data)

        # Get the actor from the database
        actor = Actor.query.filter(Actor.id == 19).one_or_none()

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        # Check for the deleted actor, total_actors and that the
        # actors return data
        self.assertTrue(data['deleted'], 19)
        # Test no longer exist
        self.assertEqual(actor, None)

    # Tests that  when a actor does not exist, an appropriate error
    # response is delivered
    def test_422_if_actor_does_not_exist(self):
        # This tests an invalid id was entered
        response = self.client().delete('/actors/100')
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unproceessable entity')

    def test_get_movies(self):
        # Make the request and process the response
        response = self.client().get('/movies')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        # Check for the total_movies and that the movies return data
        self.assertTrue(data['recent_movies'])
        self.assertTrue(len(data['recent_movies']))
        self.assertTrue(data['upcoming_movies'])
        self.assertTrue(len(data['upcoming_movies']))
    
    # Tests that a movie can be created and is successful
    def test_post_new_movies(self):
        # Create variable for mock data to use as payload for post request
        self.new_movie = {
            "title": "Test title",
            "release_date": "26/02/2021",
            "image_link": "Test Image_ink"
        }
        # Creates the new movie and loads the response data
        response = self.client().post('/movies/add', json=self.new_movie)
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        # Check for the created actor, total_movies and that the
        # movies return data
        self.assertTrue(data['total_movies'])
        self.assertTrue(len(data['movies']))

    # Tests that  when a movie is not created, an appropriate error
    # response is delivered
    def test_400_if_movie_does_not_create(self):
        # Create variable for mock movie data to use as payload for failed
        # add request
        self.new_movie = {
            "title": "",
            "release_date": "",
            "image_link": "https://www.google.com/"
        }
        # make request and process response
        response = self.client().post('/movies/add', json=self.new_movie)
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    def test_update_movie_release_date(self):
        # Updates the movie and loads the response data
        response = self.client().patch('/movies/10', json={'release_date': '20/05/2021'})
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # Tests that when an movie is not updated, an appropriate error
    # response is delivered
    def test_400_movie_for_failed_update(self):
        # Update variable for mock movie data to use as payload for failed
        # patch request
        # make request and process response
        response = self.client().patch('/movies/10')
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    # Tests that  when a movie is deleted and is successful that it returns
    # appropriate response
    def test_delete_movie(self):
        # Delete the movie and process response
        response = self.client().delete('/movies/9')
        data = json.loads(response.data)

        # Get the movie from the database
        movie = Movie.query.filter(Movie.id == 9).one_or_none()

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        # Check for the deleted movie, total_movies and that the
        # movies return data
        self.assertTrue(data['deleted'], 9)
        # Test no longer exist
        self.assertEqual(movie, None)

    # Tests that  when a movie does not exist, an appropriate error
    # response is delivered
    def test_422_if_movie_does_not_exist(self):
        # This tests an invalid id was entered
        response = self.client().delete('/movies/100')
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unproceessable entity')

    def test_get_contact(self):
        response = self.client().get('/contact')
        # Check the status code and message
        self.assertEqual(response.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

