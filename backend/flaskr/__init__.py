################################################
#  Imports                                     #
################################################

import os
from flask import Flask, json, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import random

from models import setup_db, Question, Category

################################################
#  Global Variables                            #
################################################

QUESTIONS_PER_PAGE = 10

################################################
#  Helper Functions                            #
################################################

##### Pagination #####
def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection]
  current_questions = questions[start:end]

  return current_questions

##### Get Categories From DB #####

def get_categories():
  category_query = Category.query.order_by(Category.id).all()
  
  categories = {category.id:category.type for category in category_query}
  
  return categories

################################################
#  Instantiate app                             #
################################################

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  -- DONE
  '''
  CORS(app)

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  -- DONE
  '''
  ################################################
  #  CORS                                        #
  ################################################

  @app.after_request
  def after_request(response):
    response.headers.add(
      'Access-Control-Allow-Headers', 
      'Content-Type,Authorization,true')
    response.headers.add(
      'Access-Control-Allow-Methods', 
      'GET,PUT,POST,PATCH,DELETE,OPTIONS')
    return response

  ################################################
  #  Endpoints                                   #
  ################################################

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  -- DONE
  '''

  """
  Route handler to retrieve all categories. It is made up of:
  1. The DB query to get all categories
  2. Check to make sure the query returns results, If not, abort action
  3. A list comprehension that uses the class method .format() that outputs 
     the DB record values to a dictionary, ready to be parsed into json
  4. A loop that grabs the value from categories.id and categories.type
     and makes these the key and value respectively of a single dictionary
     (the output of the list comprehension was a list of dictionaries)
  5. Return all of this as josn object that can be used by the front end
  """
  @app.route('/categories', methods=['GET'])
  def retrieve_categories():
    categories = get_categories()

    if categories is {}:
      abort(404)

    return jsonify({
      'success': True,
      'categories': categories
    })

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions', methods=['GET'])
  def retrieve_questions():
    selection = Question.query.all()
    current_questions = paginate_questions(request, selection)

    if len(current_questions) == 0:
      abort(404)
    
    categories = get_categories()
    
    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questons': len(selection),
      'categories': categories,
      'current_category': None
    })


  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  -- DONE
  '''

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None:
        abort(404)
      
      question.delete()

      return jsonify({
        'success': True
      })
    
    except:
      abort(422)

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  ################################################
  #  Error Handlers                              #
  ################################################

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found: server cannot find the requested resource."
        }), 404
  
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
        "success": False, 
        "error": 422,
        "message": "Request is unprocessable."
        }), 422
  
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
        "success": False, 
        "error": 400,
        "message": "Bad client request."
        }), 400

  @app.errorhandler(403)
  def forbidden(error):
    return jsonify({
        "success": False, 
        "error": 403,
        "message": "Access forbidden."
        }), 403
  
  @app.errorhandler(500)
  def server_error(error):
    return jsonify({
        "success": False, 
        "error": 500,
        "message": "Internal server error."
        }), 500
  
  @app.errorhandler(405)
  def not_allowed(error):
    return jsonify({
        "success": False, 
        "error": 405,
        "message": "Request method not allowed."
        }), 405

  return app

    