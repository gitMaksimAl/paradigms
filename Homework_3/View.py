from numpy import array
from abc import ABC


class View(ABC):

    def print_field(self, filed):
        ...

    def print_info(self, info):
        ...

    def refresh(self, field):
        ...


class ConsoleView(View):

    menu: str = "Please enter number of the cell to place your mark "
    usage: str = "Usage:\n\tscript [gamer]\n\t" \
        "gamer - player two, can be <ai> or <console>."
    warning: str = "Invalid parameters set."

    def print_field(self, field2d: array) -> None:
        i = 0
        while i < len(field2d) - 1:
            print(' | '.join([chr(j) for j in field2d[i]]))
            print('---' * len(field2d))
            i += 1
        print(' | '.join([chr(j) for j in field2d[i]]))

    def print_info(self, info: str) -> None:
        print(f"\n*************************\n{info}\n")

    def refresh(self, field2d: array) -> None:
        print("\033[H\033[2J")
        self.print_field(field2d)
