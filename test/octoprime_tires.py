import unittest
from tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire = OctoprimeTire([0.1, 0.3, 0.5, 0.9])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = OctoprimeTire([0.1, 0.2, 0.5, 0.7])
        self.assertFalse(tire.needs_service())