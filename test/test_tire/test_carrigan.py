import unittest

from tire_carrigan import Carrigan


class TestCarriganEngine(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.1, 0.9, 0.4, 1]
        tire = Carrigan(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.5, 0.4, 0]
        tire = Carrigan(tire_wear)
        self.assertFalse(tire.needs_service())
