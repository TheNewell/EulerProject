matrix = []


def readfile(filename, action="r"):
    file = open(filename, action)
    i = 0
    for line in file:
        row = line.split(',')
        # print(row[0])
        i += 1
        matrix.append(row)
    # print(matrix)


def nextmove(currentindex, path):
    currentrow = currentindex[0]
    currentcolumn = currentindex[1]
    move = None
    # left
    if currentcolumn - 1 > 0 and [currentindex[0], currentindex[1]-1] not in path:
        left = {
            "value": int(matrix[currentrow][currentcolumn - 1]),
            "index": [currentrow, currentcolumn - 1]
        }
        move = left

    # right
    if currentcolumn + 1 < 80 and [currentindex[0], currentindex[1]+1] not in path:
        right = {
            "value": int(matrix[currentrow][currentcolumn + 1]),
            "index": [currentrow, currentcolumn + 1]
        }
        if move is None or move["value"] > right["value"]:
            move = right
    # up
    if currentrow - 1 > 0 and [currentindex[0] - 1, currentindex[1]] not in path:
        up = {
            "value": int(matrix[currentrow - 1][currentcolumn]),
            "index": [currentrow - 1, currentcolumn]
        }
        if move is None or move["value"] > up["value"]:
            move = up
    # down
    if currentcolumn + 1 < 80 and [currentindex[0] + 1, currentindex[1]] not in path:
        down = {
            "value": int(matrix[currentrow + 1][currentcolumn]),
            "index": [currentrow + 1, currentcolumn]
        }
        if move is None or move["value"] > down["value"]:
            move = down
    return move


def pathSum(filename, frstmove, scndmove, thrdmove, frthmove):
    readfile(filename)
    currentindex = [0, 0]
    path = [currentindex]
    total = int(matrix[0][0])
    # print(int(matrix[0][0]) + int(matrix[1][0]))
    while currentindex is not matrix[-1][-1]:
        next = nextmove(currentindex, path)
        path.append(currentindex)
        currentindex = next["index"]
        total += int(next["value"])
        print(next)
        # print(total)
