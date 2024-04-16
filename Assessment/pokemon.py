class Pokemon:
    def __init__(self, id: int, name: str, height: float, weight: float):
        self._id = id
        self._name = name
        self._height = height
        self._weight = weight

    def __repr__(self) -> str:
        return f"Pokemon(ID: {self._id}, Name: {self._name}, Height: {self._height}, Weight: {self._weight})"