# Backend - Full Stack Trivia API 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
You will need to have installed Postgres. For Mac users, you can use the popular package manager [Homebrew](https://brew.sh/). Once installed, you can start, stop and restart Postgres from your terminal:

```bash
brew services start postgresql
brew services stop postgresql
brew services restart postgresql
```

Once you have Postgres installed and running, restore a database using the trivia.psql file provided. From the `backend` folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `backend` directory first ensure you are working using your created virtual environment e.g.

```bash
# activating the virtual environment
source .venv/bin/activate

# deactivating the virtual environment
deactivate
```

To run the server, execute:

```bash
FLASK_APP=flaskr FLASK_ENV=development flask run
```
The `FLASK_APP=flaskr` variable and value tells Flask to use the `flaskr` directory and will automatically use `__init__.py` as the location of the application.

The `FLASK_ENV=development` variable and value will tell Flask to look out for file updates/changes and will then restart the server. This is a setting that you would not use in production systems.

`flask run` will start up the Flask application and the server.

## ToDo Tasks
These are the files you'd want to edit in the backend:

1. *./backend/flaskr/`__init__.py`*
2. *./backend/test_flaskr.py*


One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 


2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 


3. Create an endpoint to handle GET requests for all available categories. 


4. Create an endpoint to DELETE question using a question ID. 


5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 


6. Create a POST endpoint to get questions based on category. 


7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 


8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 


9. Create error handlers for all expected errors including 400, 404, 422 and 500. 



## Review Comment to the Students
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/api/v1.0/categories'
GET ...
POST ...
DELETE ...

GET '/api/v1.0/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```
## API Reference
### Getting started
#### Base URL
At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration.
#### Authentication
This version of the application does not require authentication or API keys.
### Error Handling
Errors are returned as JSON objects in the following format:
```json
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:

* `404`: Resource Not Found
* `422`: Not Processable
* `500`: Server Error

### Endpoints
#### GET /categories
* General:
    * Returns a list of all the categories, along with a success value
    * Sample cURL: `curl -X GET http://127.0.0.1:5000/categories`
##### Sample response
```json
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```

#### GET /questions
* General:
    * Returns:
        * a list of all the categories
        * a paginated list of questions (10 per page)
        * a total count of all questions available
        * a success value
    * Sample cURL: `curl -X GET http://127.0.0.1:5000/questions`
##### Sample response
```json
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "num_questions": 10, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 23
}
```

#### DELETE /questions/{question_id}
* General:
    * Will delete a specific question using the question's ID
    This will return the ID of the deleted question and a success value
    * Sample cURL: `curl -X DELETE http://127.0.0.1:5000/questions/4`
##### Sample response
```json
{
  "deleted_question_id": 4, 
  "success": true
}
```

#### POST /questions
* General:
    * Creates a new question in the database - this includes a question, answer, a category id and a difficulty rating
    * Returns a success value and the question values posted
    * Sample cURL: `curl -X POST http://127.0.0.1:5000/questions -d '{"question": "Is this a question?", "answer": "This is an answer", "difficulty": 1, "category": "1"}' -H 'Content-Type: application/json'`
##### Sample response
```json
{
  "answer": "This is an answer", 
  "category": "1", 
  "difficulty": 1, 
  "question": "Is this a question?", 
  "success": true
}
```

#### POST /questions/search
* General:
    * Returns a list of all the categories, along with a success value and the total number of questions
    * Sample cURL: `curl -X POST http://127.0.0.1:5000/questions/search -d '{"searchTerm":"boxer"}' -H 'Content-Type: application/json'`
##### Sample response
```json
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }
  ], 
  "success": true, 
  "total_questions": 1
}
```

#### GET /categories/{category_id}/questions
* General:
    * Returns:
        * a list of all the questions within a selected category
        * a list of all the categories
        * the total number of questions returned
        * a success value
    * Sample cURL: `curl -X GET http://127.0.0.1:5000/categories/3/questions`
##### Sample response
```json
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}
```

#### POST /quizzes
* General:
    * The user plays a quiz by selecting a category and going through all the questions randomly in that category
    * Returns a randomly selected question from a bank of questions based on a selected category while checking that the question has not been asked during the quiz session
    * Also returns a success value
    * Sample cURL: `curl -X POST http://127.0.0.1:5000/quizzes -d '{"quiz_category": {"type": "Geography", "id": "3"},"previous_questions":[13, 14]}' -H 'Content-Type: application/json'`
##### Sample response
```json
{
  "question": {
    "answer": "Agra", 
    "category": 3, 
    "difficulty": 2, 
    "id": 15, 
    "question": "The Taj Mahal is located in which Indian city?"
  }, 
  "success": true
}

```



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
