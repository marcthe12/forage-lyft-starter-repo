import unittest
from tire import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire = CarriganTires([0.1, 0.3, 0.5, 0.9])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = CarriganTires([0.1, 0.2, 0.5, 0.8])
        self.assertFalse(tire.needs_service())