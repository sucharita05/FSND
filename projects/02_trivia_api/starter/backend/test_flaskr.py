import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # Test that all the categories and get success
    def test_get_categories(self):
        self.categories = {
            "1": 'Science', "2": 'Art', "3": 'Geography', "4": 'History',
            "5": 'Entertainment', "6": 'Sports'
        }
        # Make the request and process the response
        response = self.client().get('/categories', json=self.categories)
        data = json.loads(response.data)
        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['total_categories'])

    # Tests that question pagination is successful
    def test_get_paginated_questions(self):
        # Make the request and process the response
        response = self.client().get('/questions?page=1')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        # Check for the total_questions and that the questions return data
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions'])) == 10

    # Tests that question pagination failure 404 is successful
    def test_404_sent_requestig_beyond_valid_page(self):
        # Send a request with bad page data and then load response
        response = self.client().get('/questions?page=100')
        data = json.loads(response.data)
        # Check the status code and message
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # Tests that a question can be created and is successful
    def test_post_new_questions(self):
        # Create variable for mock data to use as payload for post request
        self.new_question = {
            "question": "Test Question",
            "answer": "Test Answer",
            "category": "2",
            "difficulty": 2
        }
        # Creates the new question and loads the response data
        response = self.client().post('/questions/add', json=self.new_question)
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        # Check for the created question, total_questions and that the
        # questions return data
        self.assertTrue(data['created'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['question']))

    # Tests that  when a question is not created, an appropriate error
    # response is delivered
    def test_400_if_question_does_not_create(self):
        # Create variable for mock question data to use as payload for failed
        # add request
        self.new_question = {
            "question": "Test Question",
            "answer": "",
            "category": "2",
            "difficulty": 2
        }
        # make request and process response
        response = self.client().post('/questions/add', json=self.new_question)
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')

    # Tests that  when a question is deleted and is successful that it returns
    # appropriate response
    def test_delete_question(self):
        # Delete the question and process response
        response = self.client().delete('/questions/24')
        data = json.loads(response.data)

        # Get the question from the database
        question = Question.query.filter(Question.id == 24).one_or_none()

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        # Check for the deleted question, total_questions and that the
        # questions return data
        self.assertTrue(data['deleted'], 21)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['question']))
        # Test no longer exist
        self.assertEqual(question, None)

    # Tests that  when a question does not exist, an appropriate error
    # response is delivered
    def test_422_if_question_does_not_exist(self):
        # This tests an invalid id was entered
        response = self.client().delete('/questions/100')
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unproceessable entity')

    # Tests that  when a search term is entered it returns a successful
    # response if it exists in the database
    def test_search_questions(self):
        # Create variable for mock searchTerm
        self.search_term = {'searchTerm': 'world'}
        # Make the request and process the response
        response = self.client().post('/questions/search', json=self.search_term)
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']), 2)

    # Tests for an empty search term is entered it returns the appropriate
    # error code
    def test_422_if_question_does_not_found(self):
        # Initiate an empty search request and process response
        self.search_term = {'searchTerm': ''}
        response = self.client().post('/questions/search', json=self.search_term)
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unproceessable entity')

    # Tests for a search term value that does not exist in the database and
    # returns the appropriate error code
    def test_404_if_question_does_not_found(self):
        # Initiate a search request for something that does not exist in the
        # database and process response
        self.search_term = {'searchTerm': 'asdfghjloiuyhgfvcb'}
        response = self.client().post('/questions/search', json=self.search_term)
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # Tests to retrieve the questions for a given category
    def test_get_category_questions(self):
        # Initiate a request for the History category with an ID of 4
        response = self.client().get('/categories/4/questions')
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        # Check for the current category, total_questions and that the
        # questions return data
        self.assertTrue(data['current_category'], 4)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']), 0)

    # Tests to retrieve the questions for a given category that does not exist
    # and return the appropriate error
    def test_404_if_question_category_does_not_found(self):
        # Send request with a category ID of 121, which does not exist
        response = self.client().get('/categories/121/questions')
        data = json.loads(response.data)

        # Check the status code and message
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    # Tests the trivia quiz game with different category questions
    def test_quiz_play(self):
        # Make the request and process the response
        response = self.client().post(
            '/quizzes',
            json={
                "quiz_category": {
                    "type": "Science",
                    "id": 1},
                "previous_questions": ["2"],
            })
        data = json.loads(response.data)

        # Get quiz questions from database
        quiz_ques = Question.query.filter(Question.category == 1).all()

        # Check the status code and message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])

    # Tests the trivia game with no data returned from the application
    def test_404_if_quiz_question_no_more_questions(self):
        # Process the response from the request without sending data
        response = self.client().post(
            '/quizzes',
            json={
                "quiz_category": {
                    "type": "Science",
                    "id": 10},
                "previous_questions": [
                    "2",
                    "4",
                    "6"],
            })
        data = json.loads(response.data)

        # Get quiz questions from database
        quiz_ques = Question.query.filter(Question.category == 10).all()

        # Check the status code and message
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
