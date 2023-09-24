class Vacancy:
    def __init__(self, title, url, salary, responsibility):
        self.title = title
        self.url = url
        self.salary = salary
        self.responsibility = responsibility

    def __str__(self):
        return f'{self.title}\n{self.url}\n{self.salary}\n{self.responsibility}\n'


class ListVacancies:
    list_of_vacancies = []
    def add_vacancy(self, vacancy):
        self.list_of_vacancies.append(vacancy)

    def sort_by_salary(self):
        pass

    def __str__(self):
        for vacancy in self.list_of_vacancies:
            print(vacancy)


