# coding=utf-8
"""
题目描述
在浏览器进行页面切换时，为了加速打开之前打开过的页面，有一种常用的算法，叫做LRU（Least Recently Used）算法。
某设备能够记录至多n
每次访问页面A时，如果页面A不在被记录的页面中，就需要一定时间来加载这个页面。


例如：
某设备最多纪录3个不同页面,若页面打开顺序先后依次为1,2,3,4,2,则打开编号为4 的页面时,编号为1 的页面将被淘汰.第二次打开编号为2的页面时，并不会淘汰任何页面。
若页面打开顺序依次为1,2,3,1,4，在打开编号为4的页面时，最后一次访问时间最早的是2号页面，因此会在记录中淘汰2号而记录4号。
现有一个最多记录n个不同页面的设备,并给出页面（以数字编号）的访问顺序。
请输出整个过程中共加载了多少次，以及在全部访问结束后，设备记录了哪些页面。
输入
第一行输入两个整数n,m(1≤n,m≤500)
接下来一行输入m个整数，描述页面访问顺序，保证页面编号是[1,m]内的正整数。
输出
第一行输出一个整数,表示加载的次数。
第二行输出n个整数，用空格隔开，表示全部访问结束后，设备记录的页面编号(编号按照升序输出)。数据保证访问过的不同页面总数大于等于n 。
注：输出的每一行最后不要输出多余的空格，否则系统会判为格式错误。
样例输入 Copy
输入样例1
3 5
1 2 3 4 1

输入样例2
3 5
1 2 3 1 4

输入样例3
3 5
1 2 2 2 3
样例输出 Copy
输出样例1
5
1 3 4

输出样例2
4
1 3 4

输出样例3
3
1 2 3
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, size):
        self.size = size
        self.linked_map = OrderedDict()

    def set(self, key, value):
        if key in self.linked_map:
            self.linked_map.pop(key)
        if self.size == len(self.linked_map):
            self.linked_map.popitem(last=False)
        self.linked_map.update({key: value})

    def get(self, key):
        value = self.linked_map.get(key)
        self.linked_map.pop(key)
        self.linked_map.update({key: value})
        return value


if __name__ == '__main__':
    cacheSize, accNum = map(int, input().split())
    c = LRUCache(cacheSize)
    cnt = 0
    inList = list(map(int, input().split()))
    for i in range(0, accNum):
        if inList[i] in c.linked_map:
            c.get(inList[i])
        else:
            c.set(inList[i], inList[i])
            cnt += 1
    res = sorted(c.linked_map.keys())
    print(cnt)
    for i in range(0, len(res) - 1):
        print(res[i], end=' ')
    print(res[len(res) - 1], end='')
