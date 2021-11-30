def is_valid_walk(walk):
    moves = {
        "n": [0,1],
        "e": [1,0],
        "s": [0,-1],
        "w": [-1,0]
        }
    total_moves=[0,0]
    # first check - is there ten moves?
    if len(walk)!=10:
        return False

    for value in walk:
        # print(value)
        # print(moves[value])
        total_moves[0] = total_moves[0] + moves[value][0]
        total_moves[1] = total_moves[1] + moves[value][1]
        # print(total_moves)
    if total_moves ==[0,0]:
        return True

    else:
        return False
