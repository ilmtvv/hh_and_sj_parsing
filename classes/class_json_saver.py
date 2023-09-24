import json


class JSONSaver:
    @staticmethod
    def add_vacancy(list_of_vacancies):
        json_vacancies = []
        for vacancy in list_of_vacancies:
            json_vacancies.append({
                'title': vacancy.title,
                'url': vacancy.url,
                'salary': vacancy.salary,
                'currency': vacancy.currency,
                'responsibility': vacancy.responsibility,
            })
        with open('vacancies.json', 'a') as file:
            json.dump(json_vacancies, file, indent=6)
