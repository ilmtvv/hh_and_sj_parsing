class Vacancy:
    def __init__(self, title, url, salary, currency, responsibility):
        self.title = title
        self.url = url
        self.salary = salary
        self.currency = currency
        self.responsibility = responsibility

    def __str__(self):
        return f'{self.title}\n{self.url}\n{self.salary} {self.currency}\n{self.responsibility}\n'


class ListVacancies:
    """
    Список экземпляров вакансий.
    """
    list_of_vacancies = []

    def add_vacancy(self, vacancy):
        self.list_of_vacancies.append(vacancy)

    def sort_by_salary(self):
        """
        Сортировка вакансий в списке по зп (от большей к меньшей).
        """
        self.list_of_vacancies.sort(key=lambda x: x.salary, reverse=True)

    def __str__(self):
        for vacancy in self.list_of_vacancies:
            return vacancy

    def ge_salary(self, user_salary):
        """
        Вывод вакансий у которых зп больше или равна введенной суммы пользователем.
        """
        for vacancy in self.list_of_vacancies:
            if vacancy.salary >= user_salary:
                print(vacancy)
