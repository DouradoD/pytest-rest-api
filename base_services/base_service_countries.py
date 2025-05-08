import requests

class BaseServiceCountries:

    def __init__(self, base_url):
        self.base_url = base_url
        self.service = requests.Session()

    def get(self, endpoint, params=None):
        url = f'{self.base_url}{endpoint}'
        response = self.service.get(url, params=params)
        return response