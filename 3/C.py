# coding=utf-8
"""
题目描述
大家都知道在电商网站上买东西时，网站会根据我们的搜索条件给出非常多的商品。这些商品会以依据某一种排序规则进行排序，依次呈现在我们面前。现在某电商网站关于书籍的排序依据有这么几项，综合、销量、出版时间、价格、用户评分。假设综合排名的规则为：首先看价格，价格低的排名靠前，如果价格相同，则看出版时间，出版的晚的排名靠前，如果这两项都相同则看销量，销量大的靠前，如果前三项均相同，最后看用户评分，用户评分高的排名靠前。
请依据此规则写一段给各个书按综合排名的程序。
输入
第一行为一个整数n(1<n<100),后面是n行书籍的数据，共7列，每列之间以空格分隔。其中第一列为书名（长度小于60且仅包含大写字母和小写字母的字符串），第二列到第七列均为大于等于0的整数，分别代表该书的销量、出版时间的年、月、日、价格和用户评分。
输出
n行，每行输出一本书的信息，与输入时格式一致（测试数据中保证没有排名一样的书籍，且所有整数均可以用int存储）。
样例输入 Copy
3
CPrimerPlus 3000 2013 12 6 60 44
ComputerSystemsAProgrammersPerspective 8000 2015 3 12 156 39
TheCProgrammingLanguage 50000 1978 2 22 5 46
样例输出 Copy
TheCProgrammingLanguage 50000 1978 2 22 5 46
CPrimerPlus 3000 2013 12 6 60 44
ComputerSystemsAProgrammersPerspective 8000 2015 3 12 156 39
"""


if __name__ == '__main__':
    menu = list()
    n = int(input())
    for i in range(n):
        info = input().split()
        info[1:] = map(int, info[1:])
        menu.append(info)
    menu.sort(key=lambda x: [x[5], -x[2], -x[3], -x[4], - x[1], -x[6]])
    for item in menu:
        print(' '.join(map(str, item)))
