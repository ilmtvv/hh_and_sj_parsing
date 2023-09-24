import os
from abc import ABC, abstractmethod

import requests as requests

from dotenv import load_dotenv


class JobPlatformAPI(ABC):
    """
    Абстрактный класс для API.
    """
    @abstractmethod
    def get_vacancies(self, text, area):
        pass

    @abstractmethod
    def search_area(self, area):
        pass


class HeadHunterAPI(JobPlatformAPI):
    url = 'https://api.hh.ru/vacancies'
    url_area = 'https://api.hh.ru/areas/113'

    def get_vacancies(self, text, area):
        params = {
            'text': text,
            'area': area,
            'per_page': 10,
        }
        response = requests.get(self.url, params=params)

        data = response.json()
        return data

    def search_area(self, area):
        """
        Поиск города в базе hh.
        """
        response = requests.get(self.url_area)
        data = response.json()

        for area_1 in data['areas']:
            if area_1['name'].lower() == area.lower():
                return area_1['id']
            else:
                for area_2 in area_1['areas']:
                    if area_2['name'].lower() == area.lower():
                        return area_2['id']
                    else:
                        for area_3 in area_2['areas']:
                            if area_3['name'].lower() == area.lower():
                                return area_2['id']
                            else:
                                return False


class SuperJobAPI(JobPlatformAPI):
    url = 'https://api.superjob.ru/2.0/vacancies'
    url_area = 'https://api.superjob.ru/2.0/towns/'
    load_dotenv()
    SJ_API_TOKEN = os.getenv('SJ_API_TOKEN')

    def get_vacancies(self, text, area):
        params = {
            'keyword': text,
            'town': area,
            'count': 10,
        }
        headers = {
            'X-Api-App-Id': self.SJ_API_TOKEN
        }
        response = requests.get(self.url, headers=headers, params=params)

        data = response.json()
        return data

    def search_area(self, area):
        params = {
            'keyword': area.title(),
        }
        headers = {
            'X-Api-App-Id': self.SJ_API_TOKEN
        }
        response = requests.get(self.url_area, headers=headers, params=params)
        data = response.json()
        if data['total'] == 0:
            return False
        else:
            return data['objects'][0]['id']
