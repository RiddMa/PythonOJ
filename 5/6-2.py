"""
6-2 计算素数和 (20分)
本题要求计算输入两个正整数x,y(x<=y，包括x,y)素数和。函数isPrime用以判断一个数是否素数，primeSum函数返回素数和。

输入格式:
输入两个整数。

输出格式:
[m-n]间的素数和

裁判测试程序样例：
/* 请在这里填写答案 */

x,y =map(int, input().split())
print(primeSum(x,y))
输入样例:
2 8
输出样例:
17
"""


def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1


def primeSum(a, b):
    sum = 0
    for i in range(a, b + 1):
        if isPrime(i) == 1:
            sum += i
    return sum


if __name__ == '__main__':
    x, y = map(int, input().split())
    print(primeSum(x, y))
