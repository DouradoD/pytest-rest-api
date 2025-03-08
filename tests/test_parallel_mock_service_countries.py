from time import sleep

from services.mock_service_countries import MockServiceCountries

def test_mock_get_service_countries_sleep_0(mocker,country_name='brazil', status_code=200):
    item_service = MockServiceCountries(base_url='https://restcountries.com/v3.1')
    response = item_service.get_mock_country(mocker, endpoint=f'/name/{country_name}')
    # it is not a good practice, but has being used to show de difference time from:
    # single worker(single execution) VS mult-workers(parallel execution)
    sleep(0)
    assert response.status_code == status_code
    assert response.json()[0]['name']['common'].lower() == country_name.lower()

def test_mock_get_service_countries_sleep_2(mocker,country_name='brazil', status_code=200):
    item_service = MockServiceCountries(base_url='https://restcountries.com/v3.1')
    response = item_service.get_mock_country(mocker, endpoint=f'/name/{country_name}')
    # it is not a good practice, but has being used to show de difference time from:
    # single worker(single execution) VS mult-workers(parallel execution)
    sleep(2)
    assert response.status_code == status_code
    assert response.json()[0]['name']['common'].lower() == country_name.lower()

def test_mock_get_service_countries_sleep_5(mocker,country_name='brazil', status_code=200):
    item_service = MockServiceCountries(base_url='https://restcountries.com/v3.1')
    response = item_service.get_mock_country(mocker, endpoint=f'/name/{country_name}')
    # it is not a good practice, but has being used to show de difference time from:
    # single worker(single execution) VS mult-workers(parallel execution)
    sleep(5)
    assert response.status_code == status_code
    assert response.json()[0]['name']['common'].lower() == country_name.lower()

def test_mock_get_service_countries_sleep_10(mocker,country_name='brazil', status_code=200):
    item_service = MockServiceCountries(base_url='https://restcountries.com/v3.1')
    response = item_service.get_mock_country(mocker, endpoint=f'/name/{country_name}')
    # it is not a good practice, but has being used to show de difference time from:
    # single worker(single execution) VS mult-workers(parallel execution)
    sleep(10)
    assert response.status_code == status_code
    assert response.json()[0]['name']['common'].lower() == country_name.lower()