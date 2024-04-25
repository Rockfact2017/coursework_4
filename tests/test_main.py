import unittest
from unittest.mock import patch
from vacancy import Vacancy
import main


class TestMain(unittest.TestCase):
    @patch('main.input', side_effect=['Software', '2'])
    @patch('main.pprint')
    @patch('main.HH.fetch_data')
    @patch('vacancy.Vacancy.save_to_json')
    def test_main(self, mock_save_to_json, mock_fetch_data, mock_pprint, mock_input):
        mock_fetch_data.return_value = [
            Vacancy("Software Engineer", "Looking for a Software Engineer", 90000),
            Vacancy("Senior Software Engineer", "Looking for a Senior Software Engineer", 130000)
        ]

        main.main()

        mock_fetch_data.assert_called_once_with('Software')
        mock_pprint.assert_called_once_with(mock_fetch_data.return_value[:2])
        mock_save_to_json.assert_called_once_with(mock_fetch_data.return_value)


if __name__ == '__main__':
    unittest.main()
