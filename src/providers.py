import requests
from typing import List
from vacancy import Vacancy

class HH:
    """
    Провайдер вакансий для HeadHunter.
    """
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def fetch_data(self, text: str) -> List[Vacancy]:
        """
        Получить вакансии с HeadHunter.

        Args:
            text (str): Поисковый запрос.

        Returns:
            List[Vacancy]: Список вакансий.
        """
        params = {
            "text": text,
            "area": "1",
            "per_page": 100
        }
        response = requests.get(url=self.url, params=params)
        return self._convert_to_vacancy(response.json())

    def _convert_to_vacancy(self, data) -> List[Vacancy]:
        """
        Преобразовать JSON-ответ от HeadHunter в список вакансий.

        Args:
            data (dict): JSON-ответ от HeadHunter.

        Returns:
            List[Vacancy]: Список вакансий.
        """
        vacancies = []
        for item in data['items']:
            salary_from = item['salary']['from'] if item['salary'] and item['salary']['from'] else 0
            vacancies.append(Vacancy(
                text=item['name'],
                description=item['snippet']['requirement'],
                salary=salary_from
            ))
        return vacancies
