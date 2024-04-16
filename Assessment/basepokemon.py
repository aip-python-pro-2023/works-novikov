class BasePokemon:
    def __init__(self, name: str):
     self._name = name

    def name(self) -> str:
     return self._name
    def __repr__(self) -> str:
     return f"BasePokemon(name='{self._name}')"
