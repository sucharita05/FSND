import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
import jose

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
db_drop_and_create_all()

## ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['GET'])
def get_drinks():
     # Get all drinks
    available_drinks = Drink.query.all()
    print(available_drinks)
    drinks = [drink.short() for drink in available_drinks]
    print(drinks)

    if len(drinks) == 0:
        abort(404)

    # Return data
    return jsonify({
    'success': True,
    "drinks": drinks
    })


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail', methods=['GET'])
def get_drinks_details():
    available_drinks = Drink.query.all()
   
    drinks = [drink.long() for drink in available_drinks]
    
    if len(drinks) == 0:
        abort(404)

    # Return data
    return jsonify({
    'success': True,
    "drinks": drinks
    })

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['POST'])
def new_drinks():
    try:
        # Get Drinks from json request
        body = request.get_json()
        if body is None:
                abort(404)
        new_title = body.get('title')
        new_recipe = body.get('recipe')
        new_drink = Drink(title=new_title, recipe=json.dumps(new_recipe))
        new_drink.insert()
        new_drink = Drink.query.filter_by(id=new_drink.id).first()
        return jsonify({
            'success': True,
            'drinks': [new_drink.long()]
        })
    except:
        abort(422)

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
def update_drinks(drink_id):
    # Get Drinks from json request
    body = request.get_json()
    update_title = body.get('title')
    update_recipe = body.get('recipe')
    update_drink = Drink.query.filter(Drink.id == drink_id).one_or_none()
    if update_drink is None:
        abort(404)
    update_drink.title = update_title
    update_title.recipe = update_recipe
    update_drink.update()
    return jsonify({
        'success': True, 
        'drinks': update_drink.long()
     })

'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
def delete_drinks(drink_id):
    try:
        # Get the drinks by id
        drink = Drink.query.filter(
              Drink.id == drink_id).one_or_none()
        
        # Abort 404 if no drinks found
        if drink is None:
          abort(404)
        # Else, delete the drink
        drink.delete()
        return jsonify({
            'success': True,
            'delete': drink_id
         })

    except:
        abort(404)


## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''
@app.errorhandler(404)
def not_found(error):
    return jsonify({
      'success': False, 
      'error': 404,
      'message': 'resource not found'
      }), 404
'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''
