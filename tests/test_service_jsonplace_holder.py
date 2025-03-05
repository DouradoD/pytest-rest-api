from services.service_jsonplace_holder import ServiceJSONPlaceHolder
from helpers.helpers import execution_time
base_url = 'https://jsonplaceholder.typicode.com'

@execution_time
def test_create_item():
    service = ServiceJSONPlaceHolder(base_url=base_url)
    endpoint = '/posts'
    response = service.post(endpoint=endpoint)
    assert  200 <= response.status_code < 300
    assert response.json()['id'] == 101

@execution_time
def test_get_item():
    service = ServiceJSONPlaceHolder(base_url=base_url)
    endpoint = '/posts/100'
    response = service.get(endpoint=endpoint)
    assert  200 <= response.status_code < 300
    assert response.json()['id'] == 100

@execution_time
def test_put_item():
    service = ServiceJSONPlaceHolder(base_url=base_url)
    endpoint = '/posts/1'
    data = {'userId': 1, 'id': 1, 'title': 'Dourado aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
    response = service.put(endpoint=endpoint, data=data)
    assert  200 <= response.status_code < 300
    assert 'Dourado' in response.json()['title']

@execution_time
def test_delete_item():
    service = ServiceJSONPlaceHolder(base_url=base_url)
    endpoint = '/posts/100'
    response = service.delete(endpoint=endpoint)
    assert  200 <= response.status_code < 300