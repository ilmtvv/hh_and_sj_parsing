from classes.class_api import HeadHunterAPI, SuperJobAPI
from classes.class_json_saver import JSONSaver
from classes.class_vacancies import ListVacancies, Vacancy

list_of_vacancies = ListVacancies()
hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()


def get_vacancies_hh(text, area):
    """
    Получение вакансий с hh.
    """

    data = hh_api.get_vacancies(text, area)
    vacancies = data.get('items', [])

    for vacancy in vacancies:
        name = vacancy.get('name')
        url = vacancy.get('alternate_url')
        salary_hh = vacancy.get('salary')

        if salary_hh is None:
            salary = 0
            currency = None
        elif salary_hh['from'] is None and salary_hh['to'] is not None:
            salary = salary_hh['to']
            currency = salary_hh['currency']
        elif salary_hh['from'] is not None and salary_hh['to'] is None:
            salary = salary_hh['from']
            currency = salary_hh['currency']
        else:
            salary = (salary_hh['from'] + salary_hh['to']) / 2
            currency = salary_hh['currency']

        responsibility = vacancy['snippet'].get('responsibility')

        list_of_vacancies.add_vacancy(Vacancy(name, url, salary, currency, responsibility))


def get_vacancies_sj(text, area):
    """
    Получение вакансий с hh.
    """

    data = sj_api.get_vacancies(text, area)
    vacancies = data.get('objects', [])

    for vacancy in vacancies:
        name = vacancy.get('profession')
        url = vacancy.get('link')

        if vacancy.get('payment_from') is None and vacancy.get('payment_to') is not None:
            salary = vacancy.get('payment_to')
        elif vacancy.get('payment_from') is not None and vacancy.get('payment_to') is None:
            salary = vacancy.get('payment_from')
        else:
            salary = (vacancy.get('payment_from') + vacancy.get('payment_to')) / 2

        currency = vacancy.get('currency')
        responsibility = vacancy.get('candidat')

        list_of_vacancies.add_vacancy(Vacancy(name, url, salary, currency, responsibility))


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

    user_salary = int(input('введите зп меньше которой вы получать не хотите '))

    list_of_vacancies.ge_salary(user_salary)
