import json

from classes.class_api import HeadHunterAPI
from classes.class_vacancies import ListVacancies, Vacancy

hh_api = HeadHunterAPI()
list_of_vacancies = ListVacancies()
data = hh_api.get_vacancies('python', 1)

vacancies = data.get('items', [])
for vacancy in vacancies:
    name = vacancy.get('name')
    url = vacancy.get('alternate_url')
    salary = vacancy.get('salary')
    responsibility = vacancy['snippet'].get('responsibility')

    list_of_vacancies.add_vacancy(Vacancy(name, url, salary, responsibility))

list_of_vacancies.__str__()

# with open('test.txt', 'a') as test_file:
#     json.dump(data, test_file, indent=6, ensure_ascii=False)
