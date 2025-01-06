import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fb2890d50bc48fe9d0cec2e5b6867e02'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '17907'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Привет'


@pytest.mark.parametrize('key, value', [('name', 'Привет'), ('trainer_id', TRAINER_ID), ('id', '182795')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value