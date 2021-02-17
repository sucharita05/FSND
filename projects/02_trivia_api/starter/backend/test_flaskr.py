import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from flaskr.__init__ import QUESTIONS_PER_PAGE


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', self.database_name)

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

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
    #Test '/categories' GET success
        self.categories = {
            "1": 'Science', "2": 'Art', "3": 'Geography', "4": 'History',
            "5": 'Entertainment', "6": 'Sports'
        }
        response = self.client().get('/categories', json=self.categories)
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories']) 
        self.assertTrue(data['total_categories'])

    def test_get_paginated_questions(self):
        response = self.client().get('/questions?page=1')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions'])) == QUESTIONS_PER_PAGE

    def test_404_sent_requestig_beyond_valid_page(self):
        response = self.client().get('/questions?page=100')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')
        

    def test_delete_question(self):
        response = self.client().delete('/questions/21')
        data = json.loads(response.data)

        question = Question.query.filter(Question.id == 21).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'], 21)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['question']))
        self.assertEqual(question, None)
    
    def test_422_if_question_does_not_exist(self):
        response = self.client().delete('/questions/100')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unproceessable entity')

    def test_post_new_questions(self):
        self.new_question = {
            "question": "Test Question",
            "answer": "Test Answer",
            "category": 2,
            "difficulty": 2
            }
        response = self.client().post('/questions/add', json=self.new_question)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['question']))

    def test_422_if_question_does_not_create(self): 
        self.new_question = {
            "question": "Test Question",
            "answer": "Test Answer",
            "category": 2,
            "difficulty": 2
            }
        response = self.client().post('/questions/add', json=self.new_question)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unproceessable entity')

    def test_search_questions(self):
        self.search_term={'searchTerm':'world'}
        response=self.client().post('/questions/search', json= self.search_term)
        data=json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']), 2)

    def test_404_if_question_does_not_found(self):
        self.search_term={'searchTerm':'asdfghjloiuyhgfvcb'}
        response = self.client().post('/questions/search', json= self.search_term)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_get_category_questions(self):
        category_id = 4
        response = self.client().get('/categories/{category_id}/questions')
        data=json.loads(response.data)
        print(data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["current_category"], 'History')
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['question']), 0)

    def test_404_if_question_category_does_not_found(self):
        category_id = 121
        response = self.client().get('/categories/{category_id}/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_quiz_play(self):
        response = self.client().post('/quizzes',
            json={
                "quiz_category": {"type": "Science", "id": 1},
                "previous_questions": ["2"],
            })
        data = json.loads(response.data)

        quiz_ques = Question.query.filter(Question.category == 1).all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["question"])

    def test_404_if_quiz_question_no_more_questions(self):
        response = self.client().post('/quizzes',
            json={
                "quiz_category": {"type": "Science", "id": 10},
                "previous_questions": ["2", "4", "6"],
            })
        data = json.loads(response.data)

        quiz_ques = Question.query.filter(Question.category == 10).all()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()