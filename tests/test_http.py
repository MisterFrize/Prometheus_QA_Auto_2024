import pytest
import requests

@pytest.mark.http
def test_first_request():
    response = requests.get('https://api.github.com/zen')
    print(f'Response text: {response.text}')

@pytest.mark.http
def test_second_request():
    response = requests.get('https://api.github.com/users/defunkt')
    response_json = response.json()
    assert response_json['name'] == 'Chris Wanstrath'
    assert response.status_code == 200
    assert response.headers['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_code_request():
    response = requests.get('https://api.github.com/users/sergii_butenko')
    assert response.status_code == 404