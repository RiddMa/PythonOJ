# encoding = utf-8
"""
题目描述
某电商在给它所有的书排序时比其他电商多了一个排序依据，就是依据书名的缩写排序。如果我们规定书名的缩写为书名中所有的大写字母，请你写一段依据此规则的排序程序。
样例解释：
TheCProgrammingLanguage的缩写为TCPL，CPrimerPlus的缩写为CPP，TheArtofComputerProgramming的缩写为TACP，ComputerSystemsAProgrammersPerspective的缩写为CSAPP
输入
第一行为一个正整数n(0<n<10000)。后边是n行，每行一个字符串，代表书名，每个字符串中仅包含大写字母和小写字母，且长度小于1000。


输出
共n行，每行为一个字符串，为排序后的书名（依据我们所说的缩写升序排列）。
样例输入 Copy
4
TheCProgrammingLanguage
CPrimerPlus
TheArtOfComputerProgramming
ComputerSystemsAProgrammersPerspective
样例输出 Copy
CPrimerPlus
ComputerSystemsAProgrammersPerspective
TheArtOfComputerProgramming
TheCProgrammingLanguage
"""


if __name__ == '__main__':
    namedict = dict()

    n = int(input())
    for i in range(n):
        bookname = input()
        upperletter = ''.join([ch for ch in bookname if ch.isupper()])
        namedict[bookname] = upperletter
    newdict = sorted(namedict.items(), key=lambda item:item[1])
    for j in range(len(newdict)):
        print(newdict[j][0])
