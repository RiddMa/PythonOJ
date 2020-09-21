# 题目描述
# 输入两个整数a和b，计算a+b的和。
# 输入
# 两个用空格分隔的整数，分别代表a和b（0<a,b<10000）。
# 输出
# a+b的和。

inputStr = input()
sourceNum = inputStr.split(" ")
print(int(sourceNum[0])+int(sourceNum[1]))
