from services.mock_service_countries import MockServiceCountries

def test_mock_get_service_countries(mocker,country_name='brazil', status_code=200):
    item_service = MockServiceCountries(base_url='https://restcountries.com/v3.1')
    response = item_service.get_mock_country(mocker, endpoint=f'/name/{country_name}')
    assert response.status_code == status_code
    assert response.json()[0]['name']['common'].lower() == country_name.lower()
