import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../example_app")))
import example

def test_add_one():
    assert example.add_one(3) == 4
