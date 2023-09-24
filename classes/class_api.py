import os
from abc import ABC, abstractmethod

import requests as requests

from dotenv import load_dotenv

class JobPlatformAPI(ABC):


    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(JobPlatformAPI):
    url = 'https://api.hh.ru/vacancies'
    def get_vacancies(self, text, area):
        params = {
            'text': text,
            'area': area,
            'per_page': 2,
        }
        response = requests.get(self.url, params=params)

        data = response.json()
        return data





class SuperJobAPI(JobPlatformAPI):
    url = 'https://api.superjob.ru/2.0/vacancies'
    load_dotenv()
    SJ_API_TOKEN = os.getenv('SJ_API_TOKEN')
    def get_vacancies(self, text, area):
        params = {
            'keyword': text,
            'town': area,
            'count': 2,
        }
        headers = {
            'X-Api-App-Id': self.SJ_API_TOKEN
        }
        response = requests.get(self.url,headers=headers, params=params, )

        data = response.json()
        return data

