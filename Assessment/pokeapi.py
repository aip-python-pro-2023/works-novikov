from pokemon import Pokemon
from basepokemon import BasePokemon
from typing import Generator, Union


class PokeAPI:

    def get_pokemon(name_or_id: Union[int, str]) -> Union[Pokemon, None]:
     pass

    def get_all(cls, get_full: bool = False) -> Generator[Union[BasePokemon, Pokemon], None, None]:
     pass