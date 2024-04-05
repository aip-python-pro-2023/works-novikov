import requests
from dataclasses import dataclass
from typing import Union, Generator, Dict


@dataclass(frozen=True)
class BasePokemon:
    name: str


@dataclass(frozen=True)
class Pokemon(BasePokemon):
    id: int
    weight: int
    height: int

class PokeAPI:
    f_url: str = 'https://pokeapi.co/api/v2'
    __cache: Dict[int, Pokemon] = {}

    @classmethod
    def get_pokemon(cls, name: Union[int, str]):

        for pokemon in cls.__cache.values():
            if pokemon.id == name or pokemon.name == name:
                return pokemon
        url: str = f'{cls.f_url}/pokemon/{name}'
        result: requests.Response = requests.get(url)
        result: dict = result.json()
        info: Pokemon = Pokemon({info['info']['name'].replace('-', '_'): info['f_info'] for info in result['info']})
        pokemon: Pokemon = Pokemon(id=result['id'],name=result['name'],weight=result['weight'],height=result['height'],info=info)
        cls.__cache[pokemon.id] = pokemon
        return pokemon

    @classmethod
    def get_all(cls, get_full=False) -> Generator[Union[BasePokemon, Pokemon], None, None]:
        url: str = f'{cls.f_url}/pokemon'
        result: dict = requests.get(url).json()
        while result['next'] is not None:
            for pokemon in result['results']:
                if get_full:
                    yield cls.get_pokemon(pokemon['name'])
                else:
                    yield BasePokemon(pokemon['name'])
            url = result['next']
            result = requests.get(url).json()

