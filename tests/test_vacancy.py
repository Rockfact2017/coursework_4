import unittest
from vacancy import Vacancy
import json
import os

class TestVacancy(unittest.TestCase):
    def setUp(self):
        self.vacancy = Vacancy("Data Scientist", "Looking for a Data Scientist", 120000)

    def test_str(self):
        self.assertEqual(str(self.vacancy), "Data Scientist - 120000")

    def test_repr(self):
        self.assertEqual(repr(self.vacancy), "Data Scientist - 120000")

    def test_lt(self):
        higher_salary_vacancy = Vacancy("Senior Data Scientist", "Looking for a Senior Data Scientist", 150000)
        self.assertTrue(self.vacancy < higher_salary_vacancy)

    def test_to_json(self):
        expected_json = {
            'text': "Data Scientist",
            'description': "Looking for a Data Scientist",
            'salary': 120000
        }
        self.assertEqual(self.vacancy.to_json(), expected_json)

    def test_save_to_json(self):
        vacs = [self.vacancy]
        Vacancy.save_to_json(vacs)
        with open('data.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[0]['text'], "Data Scientist")
        os.remove('data.json')

if __name__ == '__main__':
    unittest.main()
