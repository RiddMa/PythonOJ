"""
7-6 模拟报数游戏（约瑟夫环问题） (10分)
有n个人围成一圈，从1开始按顺序编号，从第一个人开始从1到k报数，报到k的人退出圈子；然后圈子缩小，从下一个人继续游戏，问最后留下的是第几号（只留1 人）。要求定义函数实现。

输入格式:
初始n和k自由指定。

输出格式:
最后留下人的原序号，以列表形式展示。

输入样例:
在这里给出一组输入。例如：

45
4
输出样例:
在这里给出相应的输出。例如：

[27]
"""


def main():
    n = eval(input())
    k = eval(input())
    liz = [i + 1 for i in range(n)]
    curn = 0
    while len(liz) > 1:
        curn = (curn + k - 1) % len(liz)
        liz.pop(curn)
    print(liz)


main()