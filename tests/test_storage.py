import unittest
import os
import json
from storage import JsonVacancyStorage
from vacancy import Vacancy

class TestJsonVacancyStorage(unittest.TestCase):
    def setUp(self):
        self.file_name = 'test_vacancies.json'
        self.storage = JsonVacancyStorage(self.file_name)
        self.vacancy = Vacancy("Web Developer", "Looking for a Web Developer", 110000)

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_add_vacancy(self):
        self.storage.add_vacancy(self.vacancy)
        with open(self.file_name, 'r') as f:
            data = json.load(f)
            self.assertEqual(data[0]['text'], "Web Developer")

    def test_get_vacancies(self):
        self.storage.add_vacancy(self.vacancy)
        criteria = {'text': "Web Developer"}
        result = self.storage.get_vacancies(criteria)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Web Developer")

    def test_delete_vacancy(self):
        self.storage.add_vacancy(self.vacancy)
        self.storage.delete_vacancy(self.vacancy)
        with open(self.file_name, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 0)

    def test_add_vacancies(self):
        vacancies = [self.vacancy, Vacancy("Frontend Developer", "Looking for a Frontend Developer", 115000)]
        self.storage.add_vacancies(vacancies)
        with open(self.file_name, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 2)

if __name__ == '__main__':
    unittest.main()
