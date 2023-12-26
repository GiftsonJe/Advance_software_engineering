import unittest
from flask import Flask, render_template, request
from app import app

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Simple Calculator", response.data)

    def test_calculate(self):
        expression = '2+2'
        response = self.app.post('/calculate', data={'expression': expression})
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"Result: {eval(expression)}".encode(), response.data)

    def test_invalid_expression(self):
        expression = 'invalid_expression'
        response = self.app.post('/calculate', data={'expression': expression})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Invalid expression", response.data)

if __name__ == '__main__':
    unittest.main()
