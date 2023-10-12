from numpy import array


class Field2d:
    """
    The field is initialized with char values and cannot be two digits long.
    Therefore, the field cannot be greater than 3x3.
    """

    def __init__(self):
        side_len = 3
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
        if x < 0 or y < 0:
            return ''
        try:
            if chr(self.__field[x][y]).isdigit():
                self.__field[x][y] = ord(char)
                self._empty = False
                return 'ack'
            else:
                return 'occupied'
        except IndexError:
            return ''

    def check(self, coords: dict) -> str:
        char, n = coords.popitem()
        if isinstance(n, int):
            xy = (n // len(self.__field), n % len(self.__field))
        else:
            xy = n
        result = self._set_char(char, xy)
        if result == 'ack':
            for line in self._variants:
                if self._check_line(line, char, xy) == 'win':
                    result = 'win'
                    break
        return result

    def _check_line(self, lines: list, char: str, xy: tuple) -> str:
        """
        Checks each pattern line indicated by the coordinate list
        against the symbol.
        :param lines: list of lists with coordinate tuples
        :param char: string with a single character
        :param xy: coords tuple
        :return:
        """
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
        # horizontal lines.
        x_variants = [(x, y) for x in range(0, end)
                      for y in range(0, end)]
        # vertical lines.
        y_variants = [(x, y) for y in range(end - 1, -1, -1)
                      for x in range(0, end)]
        # side diagonal of the matrix
        z_variant = [(x, x) for x in range(0, end)]
        # main diagonal of the matrix
        s_variant = [(x, (end - 1) - x) for x in range(0, end)]
        # grouping and add to instance.
        self._variants.append([z_variant, s_variant])
        self._variants.append([x_variants[i: i + end]
                               for i in range(0, len(x_variants), end)])
        self._variants.append([y_variants[i: i + end]
                               for i in range(0, len(y_variants), end)])
        # central and corners coordinates for some AI
        self._center = (end // 2, end // 2)
        self._corners = [(0, 0), (0, end), (end, 0), (end, end)]

    @property
    def center(self) -> tuple:
        return self._center

    @property
    def corners(self) -> list:
        return self._corners

    @property
    def empty(self) -> bool:
        return self._empty

    @property
    def variants(self):
        return self._variants
