from helpers.helpers import get_json_value
from base_services.base_service_countries import BaseServiceCountries

class MockServiceCountries(BaseServiceCountries):

    def __init__(self,base_url):
        super().__init__(base_url)

    def get_mock_country(self, mocker, endpoint):
        # create a mock API country
        mock_api_countries = mocker.Mock()

        # read file to get the mock json response
        json_response = get_json_value('data/mock_data.json')
        # Mock the response of the API country
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = json_response['service']['countries']['method']['get']
        # Set the mock API country to return the mocked response
        mock_api_countries.get.return_value = mock_response
        # Call the function with the mock API country
        return mock_api_countries.get(base_url=self.base_url, endpoint=endpoint)