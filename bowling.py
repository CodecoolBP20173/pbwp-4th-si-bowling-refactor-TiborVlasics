def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for roll in range(len(game)):
        if game[roll] == '/':
            result += 10 - last_roll
        else:
            result += get_score_for_roll(game[roll])
        if frame < 10 and game[roll] in '/Xx':
            result += get_score_for_roll(game[roll+1])
            if game[roll].lower() == 'x':
                if game[roll+2] == '/':
                    result += 10 - get_score_for_roll(game[roll+1])
                else:
                    result += get_score_for_roll(game[roll+2])
        last_roll = get_score_for_roll(game[roll])

        if not in_first_half or game[roll].lower() == 'x':
            frame += 1
            in_first_half = True
        else:
            in_first_half = False
    return result


def get_score_for_roll(char):
    if char in "123456789":
        return int(char)
    elif char in "Xx/":
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
