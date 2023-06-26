import unittest
from engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())