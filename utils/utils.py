from classes.class_api import HeadHunterAPI, SuperJobAPI
from classes.class_json_saver import JSONSaver
from classes.class_vacancies import ListVacancies, Vacancy

list_of_vacancies = ListVacancies()
hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()


def get_vacancies_hh(text, area):

    data = hh_api.get_vacancies(text, area)
    vacancies = data.get('items', [])

    for vacancy in vacancies:
        name = vacancy.get('name')
        url = vacancy.get('alternate_url')
        salary = vacancy.get('salary')
        responsibility = vacancy['snippet'].get('responsibility')

        list_of_vacancies.add_vacancy(Vacancy(name, url, salary, responsibility))


def get_vacancies_sj(text,area):

    data = sj_api.get_vacancies(text, area)
    vacancies = data.get('objects', [])

    for vacancy in vacancies:
        name = vacancy.get('profession')
        url = vacancy.get('link')
        salary = vacancy.get('payment_from')
        responsibility = vacancy.get('candidat')

        list_of_vacancies.add_vacancy(Vacancy(name, url, salary, responsibility))


def main():
    while True:
        user_input_area = input('введите город ')
        area_hh = hh_api.search_area(user_input_area)
        area_sj = sj_api.search_area(user_input_area)
        if area_hh or area_sj:
            break

    text = input('введите ключевое слово в вакансии ')

    if area_hh:
        get_vacancies_hh(text, area_hh)
    if area_sj:
        get_vacancies_sj(text, area_sj)

    list_of_vacancies.sort_by_salary()

    json_saver = JSONSaver()
    json_saver.add_vacancy(list_of_vacancies.list_of_vacancies)



