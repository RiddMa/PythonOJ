# 题目描述
# 我们都知道，在一群人里通常会有很多具有相同姓氏的人。现在就请你写一段程序，输出某群人里所有某一姓氏的人的名。
# 输入
# 第一行为一个整数n(0<n<=1000)
# 后边是n行，每行均为两个用空格分隔的字符串，为一个人的名字，其中前边的字符串代表名，后边的字符串代表姓。
# 第n+2行为一个字符串，代表待查询的姓 x。
# 输出
# 若干行，每行一个名，为输入中所有姓x的人的名。如果有多人，则按字典序输出。
# 测试用例保证1、输入中出现的所有字符串都只包含小写字母，而且长度不会超过10；2、至少有一行输出。
# 样例输入 Copy
# 4
# san zhang
# si li
# xiaoer wang
# mazi wang
# wang
# 样例输出 Copy
# mazi
# xiaoer


nameNum = int(input())
nameList = []
for i in range(0, nameNum):
    inputName = input().split(" ")
    nameList.append(inputName)
nameList.sort()

targetLastName = input()
for i in range(0, nameNum):
    if nameList[i][1] == targetLastName:
        print(nameList[i][0])
