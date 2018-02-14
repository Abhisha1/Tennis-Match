ADVANTAGE = 4
FORTY = 3
GAME_WIN = 5
POTENTIAL_WIN = 4
DUECE_GAP = 2

SCORES = {0:'0', 1: '15', 2: '30', FORTY: '40', ADVANTAGE: 'Ad',
               GAME_WIN: 'W'}

def comp101_game(points, server):
    game_score = [0, 0]
    official_score = ['0', '0']
    other_plyr = (server + 1) % 2
    i = 0
    rem = []
    winner = None
    # calculates scores of players from input data (points)
    for a in points:
        b = (a+1) % 2
        game_score[a] += 1
        i = i + 1
        #checks an incomplete game that hasn't been won without deuce
        if (game_score[a] < POTENTIAL_WIN) and (game_score[b] < POTENTIAL_WIN):
            official_score[a] = SCORES[game_score[a]]
            official_score[b] = SCORES[game_score[b]]
        # a game won without deuce
        elif (game_score[a] == POTENTIAL_WIN) and (game_score[b] < POTENTIAL_WIN - 1):
            rem = points[i:]
            winner = a
            official_score[a] = SCORES[GAME_WIN]
            official_score[b] = SCORES[game_score[b]]
            break
        else:
            # game at 40 all
            if (game_score[a] == game_score [(a+1)%2]):
                official_score[a] = SCORES[FORTY]
                official_score[b] = SCORES[FORTY]
            # game won from deuce point
            elif ((game_score[a] - game_score[(a+1)%2]) == DUECE_GAP):
                official_score[a] = SCORES[GAME_WIN]
                official_score[b] = SCORES[FORTY]
                rem = points[i:]
                winner = a
                break
            #incomplete game at deuce
            else:
                official_score[a] = SCORES[ADVANTAGE]
                official_score[b] = SCORES[FORTY]
    return '{}-{}'.format(official_score[server], official_score[other_plyr]), winner, rem


