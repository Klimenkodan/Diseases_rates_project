from diseas import Disease
import unittest


class TestDisease(unittest.TestCase):

    NEW_DISEASE = Disease('Non-Injury: Tuberculosis')

    def test_average_value(self):
        self.assertEqual(self.NEW_DISEASE.average_value(), 126)

    def test_max_value(self):
        self.assertEqual(self.NEW_DISEASE.max_value()[0], 193)

    def test_min_value(self):
        self.assertEqual(self.NEW_DISEASE.min_value()[0], 63)

    def test_average_changing(self):
        self.assertEqual(self.NEW_DISEASE.average_changing(), 'Annual decrease is: 8 people\n')

    def test_predicting(self):
        self.assertAlmostEqual(*self.NEW_DISEASE.predicting(2018), 65, msg=None, delta=0.5)


