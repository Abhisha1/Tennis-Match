WINNING_TIEBREAK_SCORE = 7
WIN_BY = 2


def comp101_tiebreaker(points, server):
    other_plyr = (server+1) % 2
    game_score = [0, 0]
    winner = None
    i = 0
    rem = []
    for a in points:
        game_score[a] += 1
        i = i + 1
        if (game_score[a] >= WINNING_TIEBREAK_SCORE) and abs(game_score[server] - game_score[other_plyr]) >= WIN_BY:
            winner = a
            rem = points[i:]
            break
    return '{}-{}'.format(game_score[server], game_score[other_plyr]), winner, rem
