# coding=utf-8
"""
题目描述
现有序列： s = 1 + a + a2 +…+ an+1
请写出递归求s的程序。
注意：此题要求递归求解，其他方式不得分
输入
只有一行，为两个用空格分隔正整数，分别代表n(0<n) 和 a(1<a)
输出
也只有一行，为此情况下s的值。（测试用例保证所有整数可以用 int存储）。
样例输入 Copy
1 2
样例输出 Copy
7
"""


def get_sum(n, a):
    if n == 0:
        return 1 + a
    else:
        return 1 + a * get_sum(n - 1, a)


if __name__ == '__main__':
    inputStr = input()
    n, a = (int(x) for x in inputStr.split(" "))
    print(get_sum(n, a))
