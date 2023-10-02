from abc import ABC


class FieldsGamer(ABC):

    # what your side white or black, X or O
    _side: str
    _name: str
    _in_game: bool

    def move(self):
        ...

    def exit(self):
        ...

    @property
    def name(self):
        return self._name


class ConsoleGamer(FieldsGamer):

    def __init__(self, actor: str, name: str):
        if actor != 'X' and actor != 'O':
            raise ValueError
        self._side = actor
        self._in_game = True
        self._name = name

    def move(self) -> dict:
        try:
            x, y = input('Your move: ').split(',')
            return {self._side: (int(x), int(y))}
        except ValueError:
            return {self._side: (-1, -1)}

    def exit(self):
        self._in_game = False


class AIGamer(FieldsGamer):

    def __init__(self, actor: str, name: str = 'AI'):
        if actor != 'X' and actor != 'O':
            raise ValueError
        self._side = actor
        self._in_game = True
        self._name = name

    def movie(self) -> tuple:
        ...
