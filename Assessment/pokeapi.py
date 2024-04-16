import requests
from typing import Generator
from pokemon import Pokemon
from base_pokemon import BasePokemon

class PokeAPI:
    @staticmethod
    def get_pokemon(identifier: str) -> Pokemon:
        url = f"https://pokeapi.co/api/v2/pokemon/{identifier.lower()}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_id = data['id']
            name = data['name']
            height = data['height']
            weight = data['weight']
            return Pokemon(id=pokemon_id, name=name, height=height, weight=weight)

    @staticmethod
    def get_all(get_full: bool = False) -> Generator[BasePokemon, Pokemon, None]:

        url = "https://pokeapi.co/api/v2/pokemon?limit=50"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for pokemon_data in data['results']:
                name = pokemon_data['name']
                if get_full:
                    pokemon = PokeAPI.get_pokemon(name)
                    yield pokemon