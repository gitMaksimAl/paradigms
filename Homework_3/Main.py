from Controller.GameController import TicTacToe
from Models.Gamer import ConsoleGamer, AIGamer
from View import ConsoleView
from Models.Field import Field2d
from sys import argv

view = ConsoleView()

if __name__ == "__main__":
    if len(argv) < 2:
        view.print_info(view.usage)
        exit(1)
    script, gamer2 = argv
    player1_name = input('Player 1 name: ')
    actor1 = input("What`s your actor? <'X' | 'O'>: ")
    player1 = ConsoleGamer(actor1, player1_name)
    actor2 = 'X' if actor1 == 'O' else 'O'
    try:
        if (gamer2 != 'console' and gamer2 != 'ai') \
                or (actor1 != 'X' and actor1 != 'O'):
            raise ValueError
    except ValueError:
        view.print_info(view.warning)
        exit(1)
    field = Field2d()
    field.set_variants()
    if gamer2 == 'console':
        player2_name = input('Player 2 name: ')
        player2 = ConsoleGamer(actor2, player2_name)
    else:
        player2 = AIGamer(field, actor2)
    game = TicTacToe(player1, player2, field, view)
    game.start()
