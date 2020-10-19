"""
题目描述
有一个n*m的矩阵(1<=n,m<=100)。开始时,矩阵的每一个元素都是0.现在,我们要对这个矩阵做Q次操作(1<=Q<=10),每次选择一个矩形区域,此区域的左上角为x1,y1,右下角为x2,y2，然后将这个矩形区域中的所有元素改为1.数据保证1<=x1<=x2<=n,1<=y1<=y2<=m.请问最后还剩下多少个元素的值为0。
输入
第一行两个整数n,m，代表矩阵的大小。 第二行一个整数Q，代表操作的次数。 接下来的Q行，每行有四个整数，x1,y1,x2,y2. 代表操作的区域。
输出
输出一个整数ans,代表最后剩余值为0的元素的个数。
样例输入 Copy
样例输入1：
2 3
3
1 1 1 2
1 2 2 2
2 2 2 3

样例输入2：
2 3
2
1 1 1 2
1 2 2 2
样例输出 Copy
样例输出1：
2

样例输出2：
3
"""

if __name__ == '__main__':
    n, m = map(int, input().split())
    op = int(input())
    zeroNum = n * m
    mat = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for it in range(op):
        x1, y1, x2, y2 = map(int, input().split())
        for row in range(x1, x2 + 1):
            for col in range(y1, y2 + 1):
                if mat[row][col] == 0:
                    zeroNum -= 1
                mat[row][col] = 1

    print(zeroNum)
