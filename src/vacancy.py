import json

class Vacancy:
    """
    Класс, представляющий вакансию.
    """
    def __init__(self, text: str, description: str, salary: int):
        """
        Инициализировать вакансию.

        Args:
            text (str): Текст вакансии.
            description (str): Описание вакансии.
            salary (int): Зарплата по вакансии.
        """
        self.text = text
        self.description = description
        self.salary = salary or 0

    def __str__(self):
        """
        Вернуть строковое представление вакансии.

        Returns:
            str: Строковое представление вакансии.
        """
        return f'{self.text} - {self.salary}\n {self.description}\n'

    def __repr__(self):
        """
        Вернуть строковое представление вакансии.

        Returns:
            str: Строковое представление вакансии.
        """
        return f'{self.text} - {self.salary}\n {self.description}\n'

    def __lt__(self, other):
        """
        Сравнить две вакансии по зарплате.

        Args:
            other (Vacancy): Другая вакансия.

        Returns:
            bool: True, если текущая вакансия имеет меньшую зарплату, чем другая вакансия, иначе False.
        """
        return self.salary < other.salary

    def to_json(self):
        """
        Вернуть JSON-представление вакансии.

        Returns:
            dict: JSON-представление вакансии.
        """
        return {
            'text': self.text,
            'description': self.description,
            'salary': self.salary
        }

    @staticmethod
    def save_to_json(vacs):
        with open('data.json', mode='w') as f:
            json.dump([v.to_json() for v in vacs], f, indent=4, ensure_ascii=False)
