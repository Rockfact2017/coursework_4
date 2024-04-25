import unittest
from unittest.mock import patch
from providers import HH
from vacancy import Vacancy

class TestHH(unittest.TestCase):
    def setUp(self):
        self.hh = HH()

    @patch('providers.requests.get')
    def test_fetch_data(self, mock_get):
        mock_response = {
            'items': [
                {
                    'name': 'Software Engineer',
                    'snippet': {'requirement': 'Experience in software development'},
                    'salary': {'from': 90000}
                }
            ]
        }
        mock_get.return_value.json.return_value = mock_response
        vacancies = self.hh.fetch_data("Software")
        self.assertEqual(len(vacancies), 1)
        self.assertIsInstance(vacancies[0], Vacancy)
        self.assertEqual(vacancies[0].text, 'Software Engineer')
        self.assertEqual(vacancies[0].salary, 90000)

if __name__ == '__main__':
    unittest.main()
