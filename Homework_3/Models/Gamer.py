from abc import ABC
from Models.Field import Field2d


class FieldsGamer(ABC):

    # what your side white or black, X or O

    def move(self):
        ...

    def exit(self):
        ...

    def name(self):
        ...


class ConsoleGamer(FieldsGamer):

    def __init__(self, actor: str, name: str):
        if actor != 'X' and actor != 'O':
            raise ValueError
        self._side = actor
        self._in_game = True
        self._name = name

    def move(self) -> dict:
        mark = {self._side: -1}
        try:
            n = int(input('Your move: '))
            mark[self._side] = n
        except ValueError:
            print('Player 1 enter wrong coordinates.')
        return mark

    @property
    def name(self):
        return self._name

    def exit(self):
        self._in_game = False


class AIGamer(FieldsGamer):
    """
    To play on another field, you need to initialize a new player.
    """

    def __init__(self, field: Field2d, actor: str, name: str = 'AI'):
        if actor != 'X' and actor != 'O':
            raise ValueError
        self._side = actor
        self._in_game = True
        self._name = name
        self._min = 0
        self._max = len(field.field) - 1
        self._field = field
        self.step = 0
        self._history = []

    def move(self) -> dict:
        """
        Tic-Tac-Toe Stupid Robot v1.0
        Optimized for 3x3 field.
        :return: dictionary with key - character and value - coords tuple
        """
        coords = [0, 0]
        mark = {self._side: -1}
        if self._field.empty:
            coords[0] = self._field.corners[self.step][0]
            coords[1] = self._field.corners[self.step][1]
        elif self.step == self._max or self.step == self._max ** 2:
            coords[0] = self._field.center[0]
            coords[1] = self._field.center[1]
        elif self._history[-4:-2] == self._history[-2:]:
            coords[0] = 0
            coords[1] = 0
        else:
            try:
                coords[0] = self._history[self.step][0]
                coords[1] = self._history[self.step][1]
            except IndexError:
                self.step -= 1
                coords[0] = self._history[self.step][0]
                coords[1] = self._history[self.step][1]
            if coords[0] < self._max:
                coords[0] += 1
            elif coords[1] < self._max:
                coords[1] += 1
            elif coords[1] > self._min:
                coords[1] -= 1
            elif coords[0] > self._min:
                coords[0] -= 1
        self._history.append(coords.copy())
        self.step += 1
        mark[self._side] = tuple(coords)
        return mark

    def exit(self) -> None:
        self.step = 0
        self._history.clear()
        self._in_game = False

    @property
    def name(self):
        return self._name
