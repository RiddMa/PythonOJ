"""
7-5 jmu-Java&Python-统计文字中的单词数量并按出现次数排序 (25分)
现在需要统计若干段文字(英文)中的单词数量，并且还需统计每个单词出现的次数。

注1：单词之间以空格(1个或多个空格)为间隔。
注2：忽略空行或者空格行。

基本版:
统计时，区分字母大小写，且不删除指定标点符号。

进阶版:

统计前，需要从文字中删除指定标点符号!.,:*?。 注意：所谓的删除，就是用1个空格替换掉相应字符。
统计单词时需要忽略单词的大小写。
输入说明
若干行英文，最后以!!!!!为结束。

输出说明
单词数量
出现次数排名前10的单词（次数按照降序排序，如果次数相同，则按照键值的字母升序排序）及出现次数。

输入样例1
failure is probably the fortification in your pole

it is like a peek your wallet as the thief when you
are thinking how to spend several hard-won lepta

when you are wondering whether new money it has laid
background because of you then at the heart of the

most lax alert and most low awareness and left it

godsend failed
!!!!!

输出样例1
46
the=4
it=3
you=3
and=2
are=2
is=2
most=2
of=2
when=2
your=2
输入样例2
Failure is probably The fortification in your pole!

It is like a peek your wallet as the thief when You
are thinking how to. spend several hard-won lepta.

when yoU are? wondering whether new money it has laid
background Because of: yOu?, then at the heart of the
Tom say: Who is the best? No one dare to say yes.
most lax alert and! most low awareness and* left it

godsend failed
!!!!!
输出样例2
54
the=5
is=3
it=3
you=3
and=2
are=2
most=2
of=2
say=2
to=2
"""


def main():
    d = dict()
    instr = ""
    trans_table = str.maketrans({'!': ' ', '.': ' ', ',': ' ', ':': ' ', '*': ' ', '?': ' '})
    while instr != "!!!!!":
        instr = input()
        lz = list(map(lambda word: word.lower(), instr.translate(trans_table).split()))
        for wd in lz:
            d[wd] = d.get(wd, 0) + 1
    print(len(d))
    for k, v in sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))[:10]:
        print(f'{k}={v}')


main()
