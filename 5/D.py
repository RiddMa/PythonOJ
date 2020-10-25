"""
6-4 修改句子 (9分)
本题参考checkio.org

读入一个英文句子，将此句子的第一个字母改为大写字母，并在最后加上句号'.'

注意：读入的句子有可能本来就符和要求。

函数接口定义：
def fun(sentence):
裁判测试程序样例：
/* 请在这里填写答案 */


doc = input()
res = fun(doc)
print(res)
输入样例1：
在这里给出一组输入。例如：

hello, world
输出样例1：
在这里给出相应的输出。例如：

Hello, world.
输入样例2：
在这里给出一组输入。例如：

Hello, world.
输出样例2：
在这里给出相应的输出。例如：

Hello, world.
"""


def fun(sentence):
    target = ""
    if sentence[0].islower():
        target += sentence[0].upper()
        target += sentence[1:]
    else:
        target += sentence
    if sentence[-1] != ".":
        target += "."
    return target


if __name__ == '__main__':
    doc = input()
    res = fun(doc)
    print(res)
