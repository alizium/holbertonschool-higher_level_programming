#!/usr/bin/python3
"""Test home page of Flask app"""

from task_01_jinja import app


def test_home_page():
    """Test that header is present in home page"""
    with app.test_client() as client:
        response = client.get('/')
        content = response.data.decode('utf-8')
        assert '<header>' in content, "Failed: Header not found in Home page"


if __name__ == "__main__":
    test_home_page()
