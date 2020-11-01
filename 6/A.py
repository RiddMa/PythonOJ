def conflict(board, nextx):
    nexty = len(board)

    for i in range(nexty):
        if abs(board[i] - nextx) in (0, nexty - i) or (nexty, nextx) == (x - 1, y - 1):
            return True
    return False


def queens(num=8, board=[]):
    for pos in range(num):
        if not conflict(board, pos):
            if len(board) == num - 1:
                # print(pos)
                yield [pos]
            else:
                for result in queens(num, board + [pos]):
                    # print(pos)
                    yield [pos] + result


x, y = input().split()
x, y = int(x), int(y)
print(len(list(queens(4))))
