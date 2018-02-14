def comp101_tiebreaker(points, server):
    score1 = 0
    score2 = 0
    i = 0
    rem = []
    for a in points:
        if a == 0:
            score1 = score1 + 1
        elif a == 1:
            score2 = score2 + 1
        else:
            print('Error in input')
            return
        i = i + 1
        if (score1 >= 7 or score2 >= 7) and abs(score1 - score2) >= 2:
            rem = points[i:]
            break
    # once score 1 or score2 hits 7, remainder index changes the points
    # so it follows tiebreaker rule
    
    t = 7
    # presents score with server 0 score first
    if server == 0:
        if score1 > 7:
            if (score1 - score2) > 2:
                # score presented in order of (game score, winner, remainder)
                return '{}-{}'.format(score1, score2), 0, rem
            elif (score1 - score2) == 2:
                return '{}-{}'.format(score1, score2), 0, rem
            if (score1 - score2) < 2:
                return '{}-{}'.format(score1, score2), None, rem
        elif score1 == 7:
                if (score1 - score2) >= 2:
                    return '{}-{}'.format(score1, score2), 0, rem
                else:
                    return '{}-{}'.format(score1, score2), None, rem
        elif score2 > 7:
                if (score2 - score1) > 2:
                    return '{}-{}'.format(score1, score2), 1, rem
                elif (score2 - score1) == 2:
                    return '{}-{}'.format(score1, score2), 1, rem
                if (score2 - score1) < 2:
                    return '{}-{}'.format(score1, score2), None, rem
        elif score2 == 7:
                if (score2 - score1) >= 2:
                    return '{}-{}'.format(score1, score2), 0, rem
                else:
                    return '{}-{}'.format(score1, score2), None, rem
        elif score1 < 7 or score2 < 7:
                return '{}-{}'.format(score1, score2), None, rem
    # presents server 1 score first
    if server == 1:
        if score1 > 7:
            if (score1 - score2) > 2:
                return '{}-{}'.format(score2, score1), 0, rem
            elif (score1 - score2) == 2:
                return '{}-{}'.format(score2, score1), 0, rem
            if (score1 - score2) < 2:
                return '{}-{}'.format(score2, score1), None, rem
        elif score1 == 7:
                if (score1 - score2) >= 2:
                    return '{}-{}'.format(score2, score1), 0, rem
                else:
                    return '{}-{}'.format(score2, score1), None, rem
        elif score2 > 7:
                if (score2 - score1) > 2:
                    return '{}-{}'.format(score2, score1), 1, rem
                elif (score2 - score1) == 2:
                    return '{}-{}'.format(score2, score1), 1, rem
                elif (score2 - score1) < 2:
                    return '{}-{}'.format(score2, score1), None, rem
        elif score2 == 7:
                if (score2 - score1) >= 2:
                    return '{}-{}'.format(score2, score1), 0, rem
                else:
                    return '{}-{}'.format(score2, score1), None, rem
        elif score1 < 7 or score2 < 7:
                return '{}-{}'.format(score2, score1), None, rem
