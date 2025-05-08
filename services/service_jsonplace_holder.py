from base_services.base_service_jsonplace_holder import BaseServiceJSONPlaceHolder
class ServiceJSONPlaceHolder(BaseServiceJSONPlaceHolder):

    def __init__(self, base_url):
        super().__init__(base_url)

    def create_item(self, endpoint, data):
        return self.post(endpoint, data)