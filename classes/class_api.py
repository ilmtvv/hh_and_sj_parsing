from abc import ABC, abstractmethod

import requests as requests


class JobPlatformAPI(ABC):


    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(JobPlatformAPI):
    url = "https://api.hh.ru/vacancies"
    def get_vacancies(self, text, area):
        params = {
            "text": text,
            "area": area,
            "per_page": 2,
        }
        response = requests.get(self.url, params=params)

        data = response.json()
        return data


