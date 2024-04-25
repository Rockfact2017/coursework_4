import json
from abc import ABC, abstractmethod
from typing import List, Dict
from vacancy import Vacancy

class AbstractVacancyStorage(ABC):
    """
    Абстрактный класс для хранения вакансий.
    """
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        """
        Добавить вакансию в хранилище.

        Args:
            vacancy (Vacancy): Вакансия для добавления.
        """
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict) -> List[Vacancy]:
        """
        Получить вакансии из хранилища, которые соответствуют заданным критериям.

        Args:
            criteria (Dict): Критерии для соответствия.

        Returns:
            List[Vacancy]: Список вакансий, соответствующих критериям.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        """
        Удалить вакансию из хранилища.

        Args:
            vacancy (Vacancy): Вакансия для удаления.
        """
        pass

class JsonVacancyStorage(AbstractVacancyStorage):
    """
    Хранилище вакансий, использующее JSON-файл.
    """
    def __init__(self, file_name: str):
        """
        Инициализировать хранилище вакансий.

        Args:
            file_name (str): Имя JSON-файла для использования.
        """
        self.file_name = file_name

    def add_vacancy(self, vacancy: Vacancy):
        """
        Добавить вакансию в хранилище.

        Args:
            vacancy (Vacancy): Вакансия для добавления.
        """
        with open(self.file_name, mode='r') as f:
            vacancies = json.load(f)
        vacancies.append(vacancy.to_json())
        with open(self.file_name, mode='w') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def get_vacancies(self, criteria: Dict) -> List[Vacancy]:
        """
        Получить вакансии из хранилища, которые соответствуют заданным критериям.

        Args:
            criteria (Dict): Критерии для соответствия.

        Returns:
            List[Vacancy]: Список вакансий, соответствующих критериям.
        """
        with open(self.file_name, mode='r') as f:
            vacancies = json.load(f)
        return [Vacancy(**vac) for vac in vacancies if all(vac[key] == value for key, value in criteria.items())]

    def delete_vacancy(self, vacancy: Vacancy):
        """
        Удалить вакансию из хранилища.

        Args:
            vacancy (Vacancy): Вакансия для удаления.
        """
        with open(self.file_name, mode='r') as f:
            vacancies = json.load(f)
        vacancies = [vac for vac in vacancies if vac['text'] != vacancy.text]
        with open(self.file_name, mode='w') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

    def add_vacancies(self, vacs: List[Vacancy]):
        """
        Добавить несколько вакансий в хранилище.

        Args:
            vacs (List[Vacancy]): Список вакансий для добавления.
        """
        with open(self.file_name, mode='r') as f:
            vacancies = json.load(f)
        vacancies.extend([v.to_json() for v in vacs])
        with open(self.file_name, mode='w') as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)
