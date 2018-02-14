WINNING_TIEBREAK_SCORE = 7
WIN_BY = 2


def comp101_tiebreaker(points, server):
    # initialize the game variables
    other_plyr = (server+1) % 2
    game_score = [0, 0]
    winner = None
    i = 0
    rem = []
    for a in points:
        #increment the game score accordingly to list of points
        game_score[a] += 1
        i = i + 1
        # checks if a player has one the tiebreak
        if (game_score[a] >= WINNING_TIEBREAK_SCORE) and abs(game_score[server] - game_score[other_plyr]) >= WIN_BY:
            winner = a
            #remaining points are indicated as remainder
            rem = points[i:]
            break
    return '{}-{}'.format(game_score[server], game_score[other_plyr]), winner, rem
