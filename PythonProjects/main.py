import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fb2890d50bc48fe9d0cec2e5b6867e02'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "ARR220999@yandex.ru",
    "password": "9224119904Abulov"
}
body_cofirmation = {
    "trainer_token": TOKEN
}
body_creat = {
    "name": "Бульбазавр11",
    "photo_id": 1
}
body_pokeball = {
    "pokemon_id": "182795"
}
body_put = {
    "pokemon_id": "182795",
    "name": "Привет",
    "photo_id": 1
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_cofirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creat)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)'''

'''message = response_pokeball.json()['message']
print(message)'''

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.text)

message = response_put.json()['message']
print(message)