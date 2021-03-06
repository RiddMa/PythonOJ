"""
6-5 矩阵乘法函数（高教社，《Python编程基础及应用》习题4-11） (5分)
设计一个Python函数，计算两个矩阵（二维列表）的乘积。

a1.png

函数接口定义：
def multiply(a,b,p,q,r)
a是一个p行q列的二维列表；b是一个q行r列的二维列表； 应返回矩阵p行r列的结果矩阵。

裁判测试程序样例：
p = int(input())
q = int(input())
r = int(input())

a = [[random.randint(0,10) for x in range(q)] for y in range(p)]
b = [[random.randint(0,10) for x in range(r)] for y in range(q)]
c = multiply(a,b,p,q,r)  #调用执行读者写的函数

rst = True

#由出题者书写的正确函数计算返回的标准答案
answerTypical = multiply1(a,b,p,q,r)
for i in range(p):
    for j in range(r):
        if c[i][j] != answerTypical[i][j]:
            rst = False
            break

print(rst)
#测试程序的正确输出
True
测试程序输入样例：
3
2
1
测试程序输出样例：
True
"""

import random


def multiply(a, b, p, q, r):
    matrix = [[0] * r for i in range(p)]
    for row in range(p):
        for col in range(r):
            for it in range(q):
                matrix[row][col] += a[row][it] * b[it][col]
    return matrix


if __name__ == '__main__':
    p = int(input())
    q = int(input())
    r = int(input())

    a = [[random.randint(0, 10) for x in range(q)] for y in range(p)]
    b = [[random.randint(0, 10) for x in range(r)] for y in range(q)]
    c = multiply(a, b, p, q, r)

    print(c)
