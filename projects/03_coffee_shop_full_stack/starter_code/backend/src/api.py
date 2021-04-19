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
# db_drop_and_create_all()

    # ROUTES
    # # Create an endpoint to handle GET drinks request
@app.route('/drinks', methods=['GET'])
def get_drinks():
    # Get all drinks
    available_drinks = Drink.query.all()
    # Get list of drinks
    drinks = [drink.short() for drink in available_drinks]
    # Abort 404 if there is no drinks
    if len(drinks) == 0:
        abort(404)

    # Return a success message
    return jsonify({
        'success': True,
        "drinks": drinks
    }), 200


    # # Create an endpoint to handle GET drinks detail request
@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_details(token):
    # Get all drinks
    available_drinks = Drink.query.all()
    # Get list of drinks detail
    drinks = [drink.long() for drink in available_drinks]
    # Abort 404 if there is no drinks
    if len(drinks) == 0:
        abort(404)

    # Return a success message
    return jsonify({
        'success': True,
        "drinks": drinks
    }), 200


    # Create an endpoint to POST a new drink
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def new_drinks(token):
    try:
        # Get Drinks from json request
        body = request.get_json()
        # Abort 404 if there is no drinks
        if body is None:
            abort(404)
        # Assign individual data from json data into variables
        new_title = body.get('title')
        new_recipe = body.get('recipe')
        # Create a new drink
        new_drink = Drink(title=new_title, recipe=json.dumps(new_recipe))
        # Insert the drink to the database
        new_drink.insert()
        # Get all drinks
        new_drink = Drink.query.filter_by(id=new_drink.id).first()
        # Return a success message
        return jsonify({
            'success': True,
            'drinks': [new_drink.long()]
        }), 200
    except BaseException:
        abort(422)


    # Create an endpoint to Update the drink using drink ID
@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drinks(payload, drink_id):
    # Get Drinks from json request
    body = request.get_json()
    try:
        update_drink = Drink.query.filter(Drink.id == drink_id).one_or_none()
        # Abort 404 if there is no drink to update
        if update_drink is None:
            abort(404)
        # Assign the data to update drink title
        update_drink.title = body.get('title', update_drink.title)
        # Assign the data to update drink recipe
        update_recipe = json.dumps(body.get('recipe'))
        if update_recipe != "null":
            update_drink.recipe = update_recipe
        else:
            update_drink.recipe
        # Update the drink
        update_drink.update()
        # Return a success message
        return jsonify({
            'success': True,
            'drinks': [update_drink.long()]
        }), 200
    except BaseException:
        abort(422)


    # Create an endpoint to DELETE drink using a drink ID.
@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(payload, drink_id):
    try:
        # Get the drinks by id
        drink = Drink.query.filter(
            Drink.id == drink_id).one_or_none()

        # Abort 404 if no drinks found
        if drink is None:
            abort(404)
        # Else, delete the drink
        drink.delete()
        # Return a success message
        return jsonify({
            'success': True,
            'delete': drink_id
        }), 200
    except BaseException:
        abort(404)


    # Create error handlers for all expected errors

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'resource not found'
    }), 404


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
