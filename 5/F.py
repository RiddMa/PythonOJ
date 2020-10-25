"""
6-6 jmu-python-发牌 (10分)
从键盘输入一个整数作为随机种子，随机生成一副扑克牌（去掉大小王），循环分给4位牌手，每人5张牌（第1、5、9、13、17张牌给第一个玩家，第2、6、10、14、18给第二个玩家。。。以此类推）并输出。

函数接口定义：
create( )
shufflecard(pokers)
deal(pokers,n)
其中create( )的功能是生成一副不含大小王的扑克牌序列并返回；shufflecard(pokers)的功能是随机洗牌并返回洗牌后的扑克牌序列，其中 pokers 是传入的参数，表示52张扑克牌的序列；deal(pokers,n) 是发5张牌给一个玩家并将发给该玩家的牌输出（输出“第i个玩家拿到的牌是：xx,xx,xx,xx,xx”，其中冒号为中文符号，5张牌之间的逗号为英文符号），其中pokers 是已经洗好牌的52张扑克牌序列、 n 表示第几个玩家。

裁判测试程序样例：
import random

/* 请在这里填写答案 */

suit=['♥','♠','♦','♣']
d=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
n=int(input())
random.seed(n)
poker=create()
poker=shufflecard(poker)
for i in range(52):
    print('%-4s'%poker[i],end='  ')
    if i%13==12:
        print()
for i in range(1,5):
    deal(poker,i)
输入样例：
7
输出样例：
♠5    ♣A    ♦6    ♥J    ♣2    ♥Q    ♥A    ♠7    ♠2    ♣Q    ♠4    ♥9    ♦K
♣6    ♦8    ♣7    ♠Q    ♦4    ♠10   ♥K    ♠9    ♣5    ♦5    ♦3    ♣J    ♣K
♥8    ♣10   ♠6    ♦10   ♥2    ♦J    ♣4    ♠3    ♣8    ♦A    ♦2    ♥6    ♥3
♠A    ♦7    ♣9    ♦Q    ♠J    ♥7    ♦9    ♥5    ♥4    ♣3    ♠K    ♥10   ♠8
第1个玩家拿到的牌是：♠5,♣2,♠2,♦K,♠Q
第2个玩家拿到的牌是：♣A,♥Q,♣Q,♣6,♦4
第3个玩家拿到的牌是：♦6,♥A,♠4,♦8,♠10
第4个玩家拿到的牌是：♥J,♠7,♥9,♣7,♥K
"""
import random


def create():
    global suit
    global d
    card_list = []
    for s in suit:
        for it in d:
            card_list.append(str(s + it))
    return card_list


def shufflecard(pokers):
    random.shuffle(poker)
    return poker


def deal(pokers, n):
    print("第{}个玩家拿到的牌是：".format(i), end='')
    temp = i
    for it in range(1, 6):
        if it <= 4:
            print('%s' % poker[temp - 1], end=',')
        else:
            print('%s' % poker[temp - 1], end='\n')
        temp += 4


if __name__ == '__main__':
    suit = ['♥', '♠', '♦', '♣']
    d = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    n = int(input())
    random.seed(n)
    poker = create()
    poker = shufflecard(poker)
    for i in range(52):
        print('%-4s' % poker[i], end='  ')
        if i % 13 == 12:
            print()
    for i in range(1, 5):
        deal(poker, i)
