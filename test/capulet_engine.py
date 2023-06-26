import unittest
from engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = CapuletEngine(30000 + 1, 0)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = CapuletEngine(30000 - 1, 0)
        self.assertFalse(engine.needs_service())