################################################
#  Imports                                     #
################################################

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

################################################
#  unittest Test Case                          #
################################################

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.test_question = {
            'question': "Some test question",
            'answer': "Some test answer",
            'difficulty': 1,
            'category': 2
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    ################################################
    #  Tests                                       #
    ################################################

    ##### Retrieve Categories Tests #####
    def test_retrieve_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    ##### Get Paginated Questions Tests #####
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])
        self.assertTrue(data['current_category'])
        self.assertEqual(data['num_questions'], 10)

    def test_404_get_paginated_questions(self):
        res = self.client().get('/questions?page=999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not found: server cannot find the requested resource.")
    
    ##### Delete Question Tests #####
    def test_delete_question(self):
        res = self.client().delete('/questions/9')
        data = json.loads(res.data)
        question = Question.query.filter(Question.id == 9).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_422_if_question_does_not_exist(self):
        res = self.client().delete('/questions/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Request is unprocessable.")
    
    ##### Create New Question Tests #####
    def test_create_question(self):
        num_questions_before = len(Question.query.all())
        res = self.client().post('/questions', json=self.test_question)
        data = json.loads(res.data)
        num_questions_after = len(Question.query.all())

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertGreater(num_questions_before, num_questions_after, "First value is not greater that second value.")

    def test_422_create_question(self):
        res = self.client().post('/questions', json={'questions': "blah"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Request is unprocessable.")


    ##### Search Questions Tests #####
    def test_search_question(self):
        res = self.client().post('/questions/search', json={'searchTerm': ""})

    ##### List Questions by Category Tests #####
    def test_get_questions_by_category(self):
        res = self.client().get('/categories/3/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])
        self.assertTrue(data['current_category'])
    
    def test_404_get_questions_by_category(self):
        res = self.client().get('/categories/999/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not found: server cannot find the requested resource.")

    ##### Play Quiz Tests #####
    def test_play_quiz(self):
        res = self.client().post('/quizzes', json={
            'quiz_category': {'type':'Science','id': 1},
            'previous_questions':[20, 21]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

    def test_404_play_quiz(self):
        res = self.client().post('/quizzes', json={
            'quiz_category': {'type':'Science','id': 1},
            'previous_questions':[20, 21, 22]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not found: server cannot find the requested resource.")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()