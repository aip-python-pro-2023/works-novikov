class BasePokemon:
    def __init__(self, name: str):
        self._name = name

    def __repr__(self) -> str:
        return f"BasePokemon(Name: {self._name})"