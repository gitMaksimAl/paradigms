from Models.Field import Field2d
from Models.Gamer import FieldsGamer
from Models.History import History
from View import View


class TicTacToe:
    player_one = None
    player_two = None
    history = None
    field = None
    view = None

    # TODO: players not used
    def __init__(self, player1: FieldsGamer,
                 player2: FieldsGamer, field: Field2d, view: View):
        self.field = field
        self.view = view
        self.history = History(player1.name, player2.name)

    def _exit(self) -> None:
        self.view.print_info(self.history.points)
        self.history.save()

    # TODO: players initialization not here
    def start(self, player1: FieldsGamer, player2: FieldsGamer) -> None:
        """
        Game start with player 1 by default if last winner not player2
        :param player1:
        :param player2:
        :return:
        """
        self.player_one = player1
        self.player_two = player2
        step = 0 if self.field.empty else 1
        stop = len(self.field.field) ** 2
        next_player = \
            player2 if player2.name == self.history.last_winner else player1
        self.view.print_field(self.field.field)
        while step != stop:
            place = self.field.check(next_player.move())
            if place == 'win':
                step = 0
                self.history.last_winner = next_player.name
                self.history.add_point(next_player.name)
                self.field.reset()
            elif place == 'occupied':
                self.view.print_info('The place is occupied.')
            elif place == 'ack':
                step += 1
                if next_player is player1:
                    next_player = player2
                else:
                    next_player = player1
                self.view.refresh(self.field.field)
            else:
                self._exit()
        else:
            self.view.print_info('Game over.')
        self._exit()
