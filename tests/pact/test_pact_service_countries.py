import atexit
import requests
from pact import Consumer, Provider
from helpers.helpers import get_json_value
from services.mock_service_countries import MockServiceCountries

pact = Consumer('Consumer').has_pact_with(
    Provider('Provider'),
    pact_dir='./pacts',
    log_dir='./logs'
)
pact.start_service()
atexit.register(pact.stop_service)

# Configuration
API_BASE_URL = "https://restcountries.com/v3.1"

def test_get_country_contract(country_name='brazil'):
    expected_response = get_json_value('data/mock_data.json')
    
    (
        pact
        .given(f'A country named {country_name} exists')
        .upon_receiving(f'A request for {country_name} data')
        .with_request('GET', f'/name/{country_name}')
        .will_respond_with(200, body=expected_response)
    )

    with pact:
        response = requests.get(f"{pact.uri}/name/{country_name}")
        assert response.status_code == 200
        assert response.json() == expected_response


def test_mock_get_service_countries(mocker,country_name='brazil', status_code=200):
    item_service = MockServiceCountries(base_url=API_BASE_URL)
    response = item_service.get_mock_country(mocker, endpoint=f'/name/{country_name}')
    assert response.status_code == status_code
    assert response.json()[0]['name']['common'].lower() == country_name.lower()

def test_mock_api_error_handling(mocker,country_name='brazil', status_code=404):
    """Test error scenarios (e.g., invalid country name)."""
    item_service = MockServiceCountries(base_url=API_BASE_URL)
    response = item_service.get_mock_country(mocker, endpoint=f'/invalid structure')
    assert response.status_code == status_code