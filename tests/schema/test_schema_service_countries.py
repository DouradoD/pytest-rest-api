import requests
import jsonschema
from services.mock_service_countries import MockServiceCountries
from helpers.helpers import get_json_value

# Real API base URL (mock API URL)
API_BASE_URL = "https://restcountries.com/v3.1"

def test_get_country(mocker,country_name='brazil', status_code=200):
    # get the schema from the json file
    user_schema = get_json_value('json_schemas/restcountries_schema.json')

    # Mock the API response
    response = MockServiceCountries(base_url=API_BASE_URL).get_mock_country(mocker, endpoint=f'/name/{country_name}')
    assert response.status_code == 200
    
    # Validate schema
    data = response.json()
    jsonschema.validate(data, user_schema)  # Raises exception if invalid
