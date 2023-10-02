from numpy import eye


class Field2d:

    def __init__(self, side_len: int):
        n = 0
        self.__field = eye(side_len, side_len, dtype='B')
        for i in range(0, side_len):
            for j in range(0, side_len):
                self.__field[i][j] = ord(str(n))
                n += 1
        self._corners = None
        self._x_variants = None
        self._y_variants = None
        self._z_variant = None
        self._s_variant = None
        self._center = None
        self._empty = True

    @property
    def field(self) -> eye:
        return self.__field

    def reset(self) -> None:
        n = 0
        for i in range(0, len(self.__field)):
            for j in range(0, len(self.__field)):
                self.__field[i][j] = ord(str(n))
                n += 1
        self._empty = True

    def set_char(self, coords: dict) -> str:
        char, xy = coords.popitem()
        x, y = xy
        try:
            if chr(self.__field[x][y]).isdigit():
                self.__field[x][y] = ord(char)
                return 'ack'
        except IndexError:
            return 'not found'

    # TODO: bad unpack items
    def check(self, coords: dict) -> str:
        char, xy = coords.popitem()
        self._check_lines(self.x_variants, char, xy)
        if
                return 'not found'

    def _check_lines(self, lines: list, char: str, xy: tuple) -> str:
        x, y = xy
        for i in self.y_variants:
            if xy in i:
                if all([chr(self.__field[j][k]) == char for j, k in i]):
                    return 'win'
                else:
                    return 'ack'
            else:
                return 'occupied'

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
        self._z_variant = [(x, x) for x in range(0, end)]
        # main diagonal of the matrix
        self._s_variant = [(x, (end - 1) - x)
                           for x in range(0, end)]
        self._x_variants = [x_variants[i: i + end]
                            for i in range(0, len(x_variants))]
        self._y_variants = [y_variants[i: i + end]
                            for i in range(0, len(y_variants))]
        self._center = (end // 2, end // 2)
        self._corners = [(0, 0), (0, end), (end, 0), (end, end)]

    @property
    def y_variants(self) -> list:
        return self._y_variants

    @property
    def x_variants(self) -> list:
        return self._x_variants

    @property
    def z_variant(self) -> list:
        return self._z_variant

    @property
    def s_variant(self) -> list:
        return self._s_variant

    @property
    def center(self) -> list:
        return self._center

    @property
    def corners(self) -> list:
        return self._corners

    @property
    def empty(self) -> bool:
        return self._empty
