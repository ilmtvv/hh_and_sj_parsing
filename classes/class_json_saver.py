import json


class JSONSaver:

    def add_vacancy(self, list_of_vacancies):
        json_vacancies = []
        for vacancy in list_of_vacancies:
            json_vacancies.append({
                'title': vacancy.title,
                'url': vacancy.url,
                'salary': vacancy.salary,
                'responsibility': vacancy.responsibility,
            })
        with open('vacancies.json', 'a', encoding='windows-1251') as file:
            json.dump(json_vacancies, file, indent=6, ensure_ascii=False)



