"""
7-2 棋盘有地雷的八皇后问题 (30分)
在国际象棋中，皇后是最厉害的棋子，可以横走、直走，还可以斜走。棋手马克斯·贝瑟尔 1848 年提出著名的八皇后问题：即在 8 × 8 的棋盘上摆放八个皇后，使其不能互相攻击 —— 即任意两个皇后都不能处于同一行、同一列或同一条斜线上。 棋盘某个格子有地雷不能放皇后，问有多少种摆法？

输入格式:
有地雷格子的坐标x和y，用空格分开

输出格式:
摆放方法的个数

输入样例:
在这里给出一组输入。例如：2 4表示第二行，第四列。

2 4
输出样例:
在这里给出相应的输出。例如：

84
"""


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


if __name__ == '__main__':
    x, y = input().split()
    x, y = int(x), int(y)
    print(len(list(queens(4))))
