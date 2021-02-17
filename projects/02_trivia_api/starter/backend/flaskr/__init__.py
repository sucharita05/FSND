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
  #Get the list component even if the index is out of range
  formatted_questions = [ques.format() for ques in selection]
  current_question = formatted_questions[start:end]
  return current_question

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  
   #Set up CORS. 

  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  
  # Create the after_request decorator to set Access-Control-Allow

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response


  
  # Create an endpoint to handle GET requests 

  @app.route('/categories', methods = ['GET'])
  def get_categories():
    # Get all categories and add to dictionary
    categories = Category.query.all()
    formatted_categories = {
      category.id: category.type
      for category in categories
    }
    # Return data
    return jsonify({
    'success' : True,
    'categories' : formatted_categories,
    'total_categories': len(categories)
    })    


  
  # Create an endpoint to handle GET requests for questions,  
  '''
  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions', methods = ['GET'])
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


  # @TODO: 
  # Create an endpoint to DELETE question using a question ID. 

  # TEST: When you click the trash icon next to a question, the question will be removed.
  # This removal will persist in the database and when you refresh the page. 

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_questions(question_id):
    try:
      # Get the question by id
      question = Question.query.filter(Question.id == question_id).one_or_none()
      
      # Abort 404 if no questions found
      if question is None :
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
    except:
      abort(422)


  # @TODO: 
  # Create an endpoint to POST a new question, 
  # which will require the question and answer text, 
  # category, and difficulty score.

  # TEST: When you submit a question on the "Add" tab, 
  # the form will clear and the question will appear at the end of the last page
  # of the questions list in the "List" tab.  

  @app.route('/questions/add', methods=['POST'])
  def create_questions():
    data = request.get_json()

    new_ques = data.get('question', '')
    new_ans = data.get('answer', '')
    new_diff = data.get('difficulty', '')
    new_cat = data.get('category', '')
        
    if ((new_ques == '') or (new_ans == '') or (new_diff == '') or (new_cat == '')):
      abort(422)

    try:
      ques = Question(
        question=new_ques,
        answer=new_ans,
        category=new_cat,
        difficulty=new_diff
        )
      ques.insert()
      selection = Question.query.order_by(Question.id).all()
      current_question = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'created': ques.id,
        'question': current_question,
        'total_questions': len(selection)
      })
    except:
      abort(422)

  # @TODO: 
  # Create a POST endpoint to get questions based on a search term. 
  # It should return any questions for whom the search term 
  # is a substring of the question. 

  # TEST: Search by any phrase. The questions list will update to include 
  # only question that include that string within their question. 
  # Try using the word "title" to start. 

  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    data = request.get_json()
    search_term = data.get('searchTerm','')

    try:
      if len(search_term) == 0:
        search_qs = Question.query.order_by(Question.id).all()
      else:
        search_query = "%{}%".format(search_term)
        search_qs = Question.query.filter(Question.question.ilike(search_query)).order_by(Question.id).all()
      current_question = paginate_questions(request, search_qs)
      return jsonify({
              'success': True, 
              'questions': current_question,
              'total_questions': len(search_qs), 
              'current_category': None
            })  
    except:
      abort(404)


  
  # @TODO: 
  # Create a GET endpoint to get questions based on category. 

  # TEST: In the "List" tab / main screen, clicking on one of the 
  # categories in the left column will cause only questions of that 
  # category to be shown. 
  
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
        formatted_questions = [ques.format() for ques in questions]
        # Return the results
        return jsonify({
            'success': True, 
            'questions': formatted_questions,
            'total_questions': len(questions), 
            'current_category': cat.type
          })


   
  # Create a POST endpoint to get questions to play the quiz. 
  
  '''
  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
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
        #if given catergory id is 0
        if quiz_category['id'] == 0:
           # Load all questions
          quiz_ques = Question.query.all()
        else:
           # Else Load questions for the choosen category
          quiz_ques = Question.query.filter(Question.category == quiz_category['id']).all()

      # Abort 422 if there is no quiz question found
      if not quiz_ques:
        return abort(422)

      selected_ques = []
      for ques in quiz_ques:
        #if questions are not in previous questions
        if ques.id not in previous_questions:
          #add new questions
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
    except:
      abort(404)
      




  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
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

    