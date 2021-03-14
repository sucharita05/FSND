import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
      # Get page value from url params
      page = request.args.get('page', 1, type=int)
      start = (page - 1) * QUESTIONS_PER_PAGE
      end = page * QUESTIONS_PER_PAGE
      # Get the list component even if the index is out of range
      formatted_questions = [ques.format() for ques in selection]
      current_question = formatted_questions[start:end]
      return current_question


def create_app(test_config=None):
      # create and configure the app
      app = Flask(__name__)
      setup_db(app)

      # Set up CORS.
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  
      # Create the after_request decorator to set Access-Control-Allow
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 
          'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 
          'GET,PATCH,POST,DELETE,OPTIONS')
      return response

  
      # Create an endpoint to handle GET requests
  @app.route('/categories', methods=['GET'])
  def get_categories():
      # Get all categories and add to dictionary
      categories = Category.query.all()
      formatted_categories = {
        category.id: category.type
        for category in categories
      }
      # Return data
      return jsonify({
      'success': True,
      'categories': formatted_categories,
      'total_categories': len(categories)
      })    


      # Create an endpoint to handle GET requests for questions
  @app.route('/questions', methods=['GET'])
  def get_questions():
      # Get all questions and paginate
      selection = Question.query.order_by(Question.id).all()
      current_question = paginate_questions(request, selection)

      # Abort 404 if no questions found
      if len(current_question) == 0:
        abort(404)
      else:
        # Get all categories and add to dictionary
        categories = {
          category.id: category.type
          for category in Category.query.order_by(Category.id).all()
        }
        # Return data
        return jsonify({
          'success': True,
          'questions': current_question,
          'categories': categories,
          'current_category': None,
          'total_questions': len(selection)
          })


      # Create an endpoint to DELETE question using a question ID.
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_questions(question_id):
      try:
        # Get the question by id
        question = Question.query.filter(
              Question.id == question_id).one_or_none()
        
        # Abort 404 if no questions found
        if question is None:
          abort(404)
        # Else, delete the question
        question.delete()
        # Get all questions and paginate
        selection = Question.query.order_by(Question.id).all()
        current_question = paginate_questions(request, selection)

        # Return data
        return jsonify({
          'success': True,
          'deleted': question_id,
          'question': current_question,
          'total_questions': len(Question.query.all())
          })
      # Abort if problem deleting question
      except Exception:
        abort(422)


      # Create an endpoint to POST a new question
  @app.route('/questions/add', methods=['POST'])
  def create_questions():
      # Get Question data from json request
      data = request.get_json()

      # Assign individual data from json data into variables
      new_ques = data.get('question', '')
      new_ans = data.get('answer', '')
      new_diff = data.get('difficulty', '')
      new_cat = data.get('category', '')

      # Validate to ensure no data is empty
      if (len(new_ques) == 0 or len(new_ans) == 0):
        abort(400)

      try:
        # Create a new question instance
        ques = Question(
          question=new_ques,
          answer=new_ans,
          category=new_cat,
          difficulty=new_diff
          )
        # Insert the question to the database
        ques.insert()
        # Get all questions and paginate
        selection = Question.query.order_by(Question.id).all()
        current_question = paginate_questions(request, selection)
        # Return a success message
        return jsonify({
          'success': True,
          'created': ques.id,
          'question': current_question,
          'total_questions': len(selection)
        })
      except Exception:
        abort(400)


      # Create a POST endpoint to get questions based on a search term.
  @app.route('/questions/search', methods=['POST'])
  def search_questions():
      # Get search term from request data
      data = request.get_json()
      search_term = data.get('searchTerm', '')
      # Abort 422 if empty search term is sent
      if len(search_term) == 0:
        abort(422)

      try:
        # Get all questions that has the search term substring
        search_query = "%{}%".format(search_term)
        search_qs = Question.query.filter(
              Question.question.ilike(search_query)).order_by(Question.id).all()

        # Abort 404 if there are no questions for search term
        if len(search_qs) == 0:
          abort(404)
        # Paginate the questions
        current_question = paginate_questions(request, search_qs)
        # Return the results
        return jsonify({
                'success': True,
                'questions': current_question,
                'total_questions': len(search_qs),
                'current_category': None
              })  
      except Exception:
        abort(404)


      # Create a GET endpoint to get questions based on category.
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def get_category_questions(category_id):
      # Get the category by id
      cat = Category.query.get(category_id)

      # Abort 404 if the category is not found
      if cat is None:
        abort(404)
      # Get the corresponding questions
      questions = Question.query.filter(Question.category == category_id).all()
      # Abort 404 if there is no question
      if len(questions) == 0:
        abort(404)
      else:
        # Paginate the questions
        current_question = paginate_questions(request, questions)
        # Return the results
        return jsonify({
            'success': True,
            'questions': current_question,
            'total_questions': len(questions),
            'current_category': category_id
          })

   
      # Create a POST endpoint to get questions to play the quiz.
  @app.route('/quizzes', methods=['POST'])
  def get_quizzes():
      # Load the request data
      data = request.get_json()
      # Get the previous questions
      previous_questions = data.get('previous_questions', [])
      # Get the category
      quiz_category = data.get('quiz_category', None)
    try:
      if quiz_category:
          # if given catergory id is 0
          if quiz_category['id'] == 0:
            # Load all questions
            quiz_ques = Question.query.all()
          else:
            # Else Load questions for the choosen category
            quiz_ques = Question.query.filter(
                  Question.category == quiz_category['id']).all()

          # Abort 422 if there is no quiz question found
          if not quiz_ques:
            return abort(422)

      selected_ques = []
      for ques in quiz_ques:
          # if questions are not in previous questions
          if ques.id not in previous_questions:
            # add new questions
            selected_ques.append(ques.format())

          # if there are still remaining questions
          if len(selected_ques) != 0:
            # Get a random question
            next_ques = random.choice(selected_ques)
            return jsonify({
              'success': True,
              'question': next_ques,
              'previous_questions': previous_questions
            })
          # No more remaining questions
          else:
            return jsonify({
              'success': False,
              'question': None,
              'previous_questions': previous_questions
            })
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

    
