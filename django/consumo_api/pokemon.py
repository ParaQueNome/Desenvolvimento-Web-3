import requests 
import json
URL = "https://pokeapi.co/api/v2/generation/1/"
req = requests.get(URL)



if req.status_code == 200:
    dados_rq = req.json()
    for pokemon in dados_rq['pokemon_species']:
        print(pokemon['name'])

    