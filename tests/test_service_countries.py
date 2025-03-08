from services.service_countries import ServiceCountries
import pytest

@pytest.mark.parametrize("country_name, status_code", [
    ('brazil', 200)
])
def test_get_service_countries(country_name, status_code):
    item_service = ServiceCountries(base_url='https://restcountries.com/v3.1')
    response = item_service.get_country(endpoint=f'/name/{country_name}')
    assert response.status_code == status_code
    assert response.json()[0]['name']['common'].lower() == country_name.lower()

def test_mock_get_service_countries(mocker,country_name='brazil', status_code=200):
    item_service = ServiceCountries(base_url='https://restcountries.com/v3.1')
    response = item_service.get_mock_country(mocker, endpoint=f'/name/{country_name}')
    assert response.status_code == status_code
    assert response.json()[0]['name']['common'].lower() == country_name.lower()
