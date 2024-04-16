class Pokemon:
    def __init__(self, id: int, name: str, height: float, weight: float):
        self._id = id
        self._name = name
        self._height = height
        self._weight = weight

    def id(self) -> int:
     return self._id

    def name(self) -> str:
     return self._name

    def height(self) -> float:
     return self._height

    def weight(self) -> float:
     return self._weight

    def __repr__(self) -> str:
     return f"Pokemon(id={self._id}, name='{self._name}', height={self._height}, weight={self._weight})"