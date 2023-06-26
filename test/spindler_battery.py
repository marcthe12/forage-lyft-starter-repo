import unittest
from batttery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        engine = SpindlerBattery(date.fromisoformat("2015-05-14"), date.fromisoformat("2020-05-15"))
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = SpindlerBattery(date.fromisoformat("2020-05-14"), date.fromisoformat("2020-05-15"))
        self.assertFalse(engine.needs_service())