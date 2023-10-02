from numpy import array


class Field2d:

    def __init__(self, side_len: int):
        self.__field = \
            array([ord(str(i)) for i in range(0, side_len ** 2)],
                  dtype='B').reshape(side_len, side_len)
        self._corners = None
        self._variants = list()
        self._center = None
        self._empty = True

    @property
    def field(self) -> array:
        return self.__field

    def reset(self) -> None:
        n = 0
        for i in range(0, len(self.__field)):
            for j in range(0, len(self.__field)):
                self.__field[i][j] = ord(str(n))
                n += 1
        self._empty = True

    def _set_char(self, char: str, xy: tuple) -> str:
        x, y = xy
        try:
            if chr(self.__field[x][y]).isdigit():
                self.__field[x][y] = ord(char)
                return 'ack'
            else:
                return 'occupied'
        except IndexError:
            return 'occupied'

    # TODO: bad unpack items
    def check(self, coords: dict) -> str:
        char, xy = coords.popitem()
        result = self._set_char(char, xy)
        if result == 'ack':
            for line in self._variants:
                if self._check_line(line, char, xy) == 'win':
                    result = 'win'
                    break
        return result

    def _check_line(self, lines: list, char: str, xy: tuple) -> str:
        for line in lines:
            if xy in line:
                if all([chr(self.__field[j][k]) == char for j, k in line]):
                    return 'win'
        else:
            return 'checked'

    def set_variants(self) -> None:
        """"
        Function calculate points on the field for wins situations
        """
        end = len(self.__field)
        y_variants = [(x, y) for x in range(0, end)
                      for y in range(0, end)]
        x_variants = [(x, y) for y in range(end - 1, -1, -1)
                      for x in range(0, end)]
        # side diagonal of the matrix
        self._variants.append([(x, x) for x in range(0, end)])
        # main diagonal of the matrix
        self._variants.append([(x, (end - 1) - x) for x in range(0, end)])
        # horizontal lines
        self._variants.append([x_variants[i: i + end]
                               for i in range(0, len(x_variants))])
        # vertical lines
        self._variants.append([y_variants[i: i + end]
                               for i in range(0, len(y_variants))])
        # central and corners coordinates for some AI
        self._center = (end // 2, end // 2)
        self._corners = [(0, 0), (0, end), (end, 0), (end, end)]

    @property
    def center(self) -> list:
        return self._center

    @property
    def corners(self) -> list:
        return self._corners

    @property
    def empty(self) -> bool:
        return self._empty
