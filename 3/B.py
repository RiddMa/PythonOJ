# coding=utf-8
"""
题目描述
因为151既是一个质数又是一个回文数（从左到右和从右到左是看一样的），所以151是回文质数。请写一个程序来找出范围[a,b] (5≤a≤b≤100000)间的所有回文质数。

输入
只有一行，为两个整数，依次代表a,b 。
输出
每个回文质数输出一行。测试用例保证输入合法且输出至少包含一个回文质数。
样例输入 Copy
100 200
样例输出 Copy
101
131
151
181
191
"""


def is_prime(num):
    flag = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(num):
    flag = 0
    if str(num) == str(num)[::-1]:
        return True
    return False


if __name__ == '__main__':
    inputStr = input()
    start, end = (int(x) for x in inputStr.split(" "))
    for j in range(start, end + 1):
        if is_palindrome(j) and is_prime(j):
            print(j)
