import unittest
from engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = WilloughbyEngine(60000 + 1, 0)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = WilloughbyEngine(60000 - 1, 0)
        self.assertFalse(engine.needs_service())