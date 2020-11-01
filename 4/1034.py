"""
题目描述
给出两个整数集合A、B，求出他们的交集、并集以及B在A中的余集。

输入
第一行为一个整数n，表示集合A中的元素个数。
第二行有n个互不相同的用空格隔开的整数，表示集合A中的元素。
第三行为一个整数m，表示集合B中的元素个数。
第四行有m个互不相同的用空格隔开的整数，表示集合B中的元素。
集合中的所有元素均为int范围内的整数，n、m<=1000。
输出
第一行按从小到大的顺序输出A、B交集中的所有元素。
第二行按从小到大的顺序输出A、B并集中的所有元素。
第三行按从小到大的顺序输出B在A中的余集中的所有元素。
样例输入 Copy
5
1 2 3 4 5
5
2 4 6 8 10
样例输出 Copy
2 4
1 2 3 4 5 6 8 10
1 3 5
"""

if __name__ == '__main__':
    ASize = int(input())
    A = set(list(map(int, input().split())))
    BSize = int(input())
    B = set(list(map(int, input().split())))

    newList = list(A & B)
    newList.sort()
    print(" ".join(map(str, newList)))

    newList.clear()
    newList = list(set((A | B)))
    newList.sort()
    print(" ".join(map(str, newList)))

    newList.clear()
    newList = list(set((A - B)))
    newList.sort()
    print(" ".join(map(str, newList)))
