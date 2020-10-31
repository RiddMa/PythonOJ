"""
6-3 黑洞数 (10分)
本题要求实现一个函数，判断某整数是否是黑洞数，如果是，返回True，否则返回False。黑洞数指的是，若某整数各个位上的数字组成的最大数减去各个位上数字组成的最小数等于该数本身，则称该数为黑洞数。比如495=954-459。

函数接口定义：
def isHd(n)
其中参数n是任意整数。

裁判测试程序样例：
/* 请在这里填写答案 */
n = int(input())
if isHd(n):
    print("yes")
else:
    print("no")
输入样例：
495
输出样例：
yes
输入样例：
1563
输出样例：
no
"""


def isHd(n):
    numStr = str(n)
    maxStr = ""
    minStr = ""
    for it in sorted(numStr, reverse=True):
        maxStr += str(it)
    for it in sorted(numStr):
        minStr += str(it)
    if int(maxStr) - int(minStr) == n:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input())
    if isHd(n):
        print("yes")
    else:
        print("no")
