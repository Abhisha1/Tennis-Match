def comp101_game(points, server):
    score1 = 0
    score2 = 0
    i = 0
    rem = []
    # score_converted changes basic scores (up to 5-3) into tennis scores
    score_converted = [
        '0-0', '0-0', '1-0', '15-0', '0-1', '0-15', '1-1', '15-15', '1-2',
        '15-30', '2-1', '30-15', '2-2', '30-30', '0-2', '0-30', '2-0', '30-0',
        '3-0', '40-0', '0-3', '0-40', '3-1', '40-15', '1-3', '15-40', '3-2',
        '40-30', '2-3', '30-40', '3-3', '40-40', '4-3', 'Ad-40', '3-4',
        '40-Ad', '5-3', 'W-40', '3-5', '40-W', '4-2', 'W-30', '2-4', '30-W',
        '4-1', 'W-15', '1-4', '15-W', '4-0', 'W-0', '0-4', '0-W'
                      ]
    # calculates scores of players from input data (points)
    for a in points:
        if a == 0:
            score1 = score1 + 1
        elif a == 1:
            score2 = score2 + 1
        else:
            print('Error in input')
            return
        # calculate the score when players enter consecutive deuce-advantage's
        i = i + 1
        if (score1 >= 5 and score2 >= 3) or (score2 >= 5 and score1 >= 3)\
           or (score1 == 4 and score2 == 4):
            # game should be won
            if abs(score1 - score2) == 2:
                if score1 > score2:
                    score1 = 5
                    score2 = 3
                elif score2 > score1:
                    score1 = 3
                    score2 = 5
            # one player at advantage
            elif abs(score1 - score2) == 1:
                if score1 > score2:
                    score1 = 4
                    score2 = 3
                elif score2 > score1:
                    score1 = 3
                    score2 = 4
            # players at deuce
            if abs(score1 - score2) == 0:
                score1 = 3
                score2 = 3
        # calculating score with remainders
        if (score1 > 3 and score2 >= 3 and abs(score1 - score2) >= 2) or\
           (score1 >= 3 and score2 > 3 and abs(score1 - score2) >= 2) or\
           (score1 >= 4 and 0 <= score2 < 3) or\
           (score2 >= 4 and 0 <= score1 < 3):
            rem = points[i:]
            points = points[:i]
            break
    g = 0
    basic_score = 0
    # server 0 presents server 0 scores first
    if server == 0:
        basic_score = '{}-{}'.format(score1, score2)
        if basic_score in score_converted:
            # score converted into tennis scoring system
            g = score_converted.index(basic_score)
            g = g + 1
            score_converted = score_converted[g]
            if 'W' in score_converted:
                if score_converted[0] == 'W':
                    return (score_converted, 0, rem)
                else:
                    return (score_converted, 1, rem)
            else:
                return (score_converted, None, [])
    elif server == 1:
        basic_score = '{}-{}'.format(score2, score1)
        if basic_score in score_converted:
            # score converted into tennis scoring system
            g = score_converted.index(basic_score)
            g = g + 1
            score_converted = score_converted[g]
            if 'W' in score_converted:
                if score_converted[0] == 'W':
                    return (score_converted, 1, rem)
                else:
                    return (score_converted, 0, rem)
            else:
                return (score_converted, None, [])
    else:
        return 'Error'
