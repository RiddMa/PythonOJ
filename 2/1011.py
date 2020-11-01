# 题目描述
# 在Linux命令行下，输入字符后，按两次Tab键，shell就会列出以这些字符打头的所有可用命令。如果只有一个命令匹配到，按一次Tab键就自动将这个命令补全。
# 比如，想更改密码，但只记得这个命令前几个字母是pass。这时候，按Tab键，shell就自动输出 passwd 命令，非常方便。现在就请你写一段程序实现类似功能。
# 输入
# 第一行为一个整数n(1<n<100)，代表共n条命令；
# 后边为n行字符串（长度均不超过50且只包含小写字母），代表这n条命令；
# 第n+2行为一个字符串（长度均不超过50且只包含小写字母），为测试字符串；
# 输出
# 若干行，为n条命令中所有以测试字符串开头的命令，每个命令占一行，按字典序依次输出。测试数据保证至少会有一条命令被输出。
# 样例输入 Copy
# 6
# ls
# cd
# cp
# rm
# mv
# diff
# c
# 样例输出 Copy
# cd
# cp


cmdList = []
cmdNum = int(input())
for i in range(0, cmdNum):
    cmdList.append(input())

cmdList.sort()

usrInput = input()
for i in range(0, cmdNum):
    if cmdList[i].startswith(usrInput):
        print(cmdList[i])
