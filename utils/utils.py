from classes.class_api import HeadHunterAPI, SuperJobAPI
from classes.class_json_saver import JSONSaver
from classes.class_vacancies import ListVacancies, Vacancy

list_of_vacancies = ListVacancies()


def get_vacancies_hh(text, area):
    hh_api = HeadHunterAPI()
    data = hh_api.get_vacancies(text, area)
    vacancies = data.get('items', [])

    for vacancy in vacancies:
        name = vacancy.get('name')
        url = vacancy.get('alternate_url')
        salary = vacancy.get('salary')
        responsibility = vacancy['snippet'].get('responsibility')

        list_of_vacancies.add_vacancy(Vacancy(name, url, salary, responsibility))


def get_vacancies_sj(text,area):
    sj_api = SuperJobAPI()
    data = sj_api.get_vacancies(text, area)
    vacancies = data.get('objects', [])

    for vacancy in vacancies:
        name = vacancy.get('profession')
        url = vacancy.get('link')
        salary = vacancy.get('payment_from')
        responsibility = vacancy.get('candidat')

        list_of_vacancies.add_vacancy(Vacancy(name, url, salary, responsibility))


def main():
    text = input('введите ключевое слово ')
    area = 70
    get_vacancies_hh(text, area)
    get_vacancies_sj(text, area)
    list_of_vacancies.__str__()
    json_saver = JSONSaver()
    json_saver.add_vacancy(list_of_vacancies.list_of_vacancies)

