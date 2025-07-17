#!/usr/bin/python3
"""Test home page of Flask app"""

import unittest
from task_01_jinja import app


class TestHomePage(unittest.TestCase):
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test that home page loads correctly"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to My Flask App', response.data)


if __name__ == '__main__':
    unittest.main()
