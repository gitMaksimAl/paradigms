from Models.Field import Field2d
from Models.Gamer import FieldsGamer
from Models.History import History
from View import View


class TicTacToe:

    # TODO: players not used
    def __init__(self, player1: FieldsGamer,
                 player2: FieldsGamer, field: Field2d, view: View):
        self.field = field
        self.view = view
        self.player_one = player1
        self.player_two = player2
        self.history = History(player1.name, player2.name)

    def _exit(self) -> None:
        self.view.print_info(self.history)
        self.history.save()

    # TODO: players initialization not here
    def start(self) -> None:
        """
        Game start with player 1 by default if last winner not player2
        :return:
        """
        step = 0 if self.field.empty else 1
        stop = len(self.field.field) ** 2
        next_player = self.player_two \
            if self.player_two.name == self.history.last_winner \
            else self.player_one
        self.view.refresh(self.field.field)
        while step != stop:
            place = self.field.check(next_player.move())
            match place:
                case 'win':
                    step = 0
                    self.history.last_winner = next_player.name
                    self.history.add_point(next_player.name)
                    self.field.reset()
                    self.view.refresh(self.field.field)
                case 'occupied':
                    self.view.print_info('Can`t be posted here.')
                case 'ack':
                    step += 1
                    if next_player is self.player_one:
                        next_player = self.player_two
                    else:
                        next_player = self.player_one
                    self.view.refresh(self.field.field)
                case _:
                    self._exit()
                    break
        else:
            self.view.print_info('Game over.')
