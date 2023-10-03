# Tic-Tac-Toe

## Description

A tic-tac-toe game with a standard 3x3 field. The game has a implementation of
a blunt bot, which needs to be improved. It can dwell on the extreme coordinates
of the field (the program will crash with an error). The field cannot be larger
than 3x3 because it is initialized with char values. After initialization, it is
important to call the set_variants function to set coordinates when checking
winning situations and the bot operation.

> Игра крестики-нолики написана в ООП парадигме т.к. имеет общие особенности
> с такими играми как шашки или шахматы, в которых есть какое-то поле X*Y,
> два игрока и акторов, которыми они управляют. Методы и свойства классов
> могут быть переопределены под данные игры.
> **_PS_**: Внимание! Не рекомендуется использовать бота при игре. Бот не
> допиленый, игра может вылететь.
