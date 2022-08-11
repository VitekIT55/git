class WrongNumberOfPlayersError(Exception):
    __module__ = Exception.__module__


class NoSuchStrategyError(Exception):
    __module__ = Exception.__module__


def rps_game_winner(game):
    if len(game) != 2:
        raise WrongNumberOfPlayersError
    #   player - pl
    pl1 = game[0][1]
    pl2 = game[1][1]
    if (pl1 != 'P' and pl1 != 'S' and pl1 != 'R') or (pl2 != 'P' and pl2 != 'S' and pl2 != 'R'):
        raise NoSuchStrategyError
    if pl1 == pl2:
        return game[0][0] + ' ' + game[0][1]
    if pl1 == 'P' and pl2 == 'R':
        win = 0
    elif pl1 == 'S' and pl2 == 'P':
        win = 0
    elif pl1 == 'R' and pl2 == 'S':
        win = 0
    else:
        win = 1
    return game[win][0] + ' ' + (game[win][1])
