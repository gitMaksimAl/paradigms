from datetime import date
from sys import stderr


class History:
    """
    Class for save games history.
    """

    points = dict()
    last_winner = None
    save_file = None

    def __init__(self, player1_name: str,
                 player2_name: str, file: str = 'history.txt'):
        try:
            self.save_file = open(file, "w")
        except IOError :
            print('Cant open history file.', file=stderr)
            exit(2)
        self.points["date"] = str(date.today())
        self.points[player1_name] = 0
        self.points[player2_name] = 0

    def add_point(self, player_name: str) -> None:
        """
        Add point to player by name and save him like last winner.
        :param player_name:
        :return:
        """
        self.points[player_name] += 1
        self.last_winner = player_name

    def save(self):
        try:
            self.save_file.write("{:>12}\t{:>12}\t{:>12}".format(*self.points)
                                 + '\n')
            self.save_file.write("{:>12}\t{:>12}\t{:>12}"
                                 .format(*self.points.values()) + '\n')
            self.save_file.close()
        except IOError:
            print('Cant write history to file.', file=stderr)

    def __str__(self):
        string = str()
        for k, v in self.points.items():
            string += f"{k}: {v}\n"
        return string
