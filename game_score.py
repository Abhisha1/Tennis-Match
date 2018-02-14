def comp101_score(points, player):
        # points presented as a list, shows sequence of game points
        # denote player 1 winning a point, 0 denote player 0 winning a point
    score1 = 0
    # score1 will represent player 0's score
    score2 = 0
    # score2 will represent player 1's score
    for a in points:
        if a == 0:
            score1 = score1 + 1
        else:
            score2 = score2 + 1
    if player == 0:
        # if player is 0, score will be presented with player 0 score first
        return score1, score2
    else:
        # if player is 1, score will be presented with player 1 score first
        return score2, score1
