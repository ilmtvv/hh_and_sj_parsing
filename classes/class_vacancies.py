class Vacancy:
    def __init__(self, name, url, salary, responsibility):
        self.name = name
        self.url = url
        self.salary = salary
        self.responsibility = responsibility

    def __str__(self):
        return f'{self.name}\n{self.url}\n{self.salary}\n{self.responsibility}\n'


class ListVacancies:
    list_of_vacancies = []
    def add_vacancy(self, vacancy):
        self.list_of_vacancies.append(vacancy)

    def __str__(self):
        for vacancy in self.list_of_vacancies:
            print(vacancy)


