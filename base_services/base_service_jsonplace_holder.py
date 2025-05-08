import requests

class BaseServiceJSONPlaceHolder:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.session()

    def get(self, endpoint, headers=None, params=None):
        url = f'{self.base_url}{endpoint}'
        return self.session.get(url=url, headers=headers, params=params)

    def post(self, endpoint, data=None, headers=None):
        url = f'{self.base_url}{endpoint}'
        return self.session.post(url=url, headers=headers, json=data)

    def put(self, endpoint, data, headers=None):
        url = f'{self.base_url}{endpoint}'
        return  self.session.put(url=url, headers=headers, json=data)

    def patch(self, endpoint, data, headers=None):
        url = f'{self.base_url}{endpoint}'
        return self.session.patch(url=url, headers=headers, json=data)

    def delete(self, endpoint, headers=None):
        url = f'{self.base_url}{endpoint}'
        return self.session.patch(url=url, headers=headers)