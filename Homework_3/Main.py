from Controller.GameController import TicTacToe
from Models.Gamer import ConsoleGamer
from View import ConsoleView
from Models.Field import Field2d

field = Field2d(3)
field.set_variants()
view = ConsoleView()
view.print_field(field.field)
player1 = ConsoleGamer('X', 'maksim')
player2 = ConsoleGamer('O', 'andrei')
game = TicTacToe(player1, player2, field, view)
print('')
# field.set_value('X', 1, 1)
# view.refresh(field.field)
# field.reset()
# view.refresh(field.field)
