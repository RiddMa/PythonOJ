def func1(*a):
    if len(a):
        avg = sum(a) / len(a)
        ans = [i for i in a if i < avg]
        return avg, ans
    return -1


if __name__ == '__main__':
    print(func1(1, 2))
