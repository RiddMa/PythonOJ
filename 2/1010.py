# 题目描述
# 给定一个字符及若干字符串。请按要求输出相应字符串。
# 输入
# 第一行为一个字符c(只可能是大写字符或小写字符)
# 第二行为一个整数n（1<n<20)，代表测试数据组数。
# 后边是n行，每行一个字符串（字符串中只包含大写字母或小写字母，且长度小于60）。
# 输出
# 若干行（至少一行），每行对应输入的n行字符串，如果c在该行字符串中出现过3次或3次以上（无论大写或小写只要字母一样就算出现一次），则该字符串被输出，
# 否则该字符串不能被输出。如果输出的字符串超过一个，则每个字符串占一行且后输入的先输出。
# 样例输入 Copy
# a
# 2
# TaNgvFRLJUvgnLjdKvaacumgGtOl
# dcaLySkOWzYyAYKBOyfIIxOZCi
# 样例输出 Copy
# TaNgvFRLJUvgnLjdKvaacumgGtOl


targetStr = input()
if targetStr.isupper():
    targetStrAlt = targetStr.lower()
else:
    targetStrAlt = targetStr.upper()

dataNum = int(input())
dataTarget = []
for dataCounter in range(0, dataNum):
    inputStr = input()
    if inputStr.count(targetStr)+inputStr.count(targetStrAlt) >= 3:
        dataTarget.append(inputStr)

dataTarget.reverse()
for targetCounter in range(0, len(dataTarget)):
    print(dataTarget[targetCounter])
