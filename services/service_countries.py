from base_services.base_service_countries import BaseServiceCountries

class ServiceCountries(BaseServiceCountries):

    def __init__(self,base_url):
        super().__init__(base_url)

    def get_country(self, endpoint):
        return self.get(endpoint=endpoint)
