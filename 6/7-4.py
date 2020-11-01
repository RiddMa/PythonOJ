"""
7-4 解析车间里的阀门状态 （高教社，《Python编程基础及应用》习题5-4） (10分)
CPU通过一个8位IO口读取了1个字节的内容，现在存储在一个bytes对象里，示例： b'\x45'；这8位分 别代表了车间里8个阀门的当前状态，1表示该阀门通，0表示该阀门断。请设计一个程序，从bytes对象解析出8个 阀门的当前状态，True表示通，False表示断。这8个状态应组织在一个列表中，其中，第i个元素对应输入字节的第i 位。

输出格式示例：[True, False, False, True, True,True,False,False]

输入格式:
形如 b'\x45'的单字节bytes。（注意是16进制）

输出格式:
包含8个布尔值的列表。其中，第i个元素代表输入字节的第i位(从低到高分别是0 ~ 7位）。

[True, False, True, False, False, False, True, False]

输入样例:
b'\x01'
输出样例:
[True, False, False, False, False, False, False, False]
"""


val = eval(input())[0]
lz = []
for i in range(8):
    lz.append(bool(val & 0x1))
    val >>= 1
print(lz)
