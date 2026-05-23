import unittest
from symptom_checker_dictionary import get_advice

class TestSymptomChecker(unittest.TestCase):
    def test_fever_contains_malaria(self):
        advice = get_advice("fever")
        self.assertIn("malaria", advice.lower())

if __name__ == "__main__":
    unittest.main()