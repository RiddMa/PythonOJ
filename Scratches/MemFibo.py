def fibo(n):
    if n == 1 or n == 2:
        ans[n] = 1
        return 1
    elif ans[n] != 0:
        return ans[n]
    else:
        ans[n - 1] = fibo(n - 1)
        ans[n - 2] = fibo(n - 2)
        return ans[n - 1] + ans[n - 2]


global ans

if __name__ == '__main__':
    ans = [0 for i in range(1000)]
    # print(fib)
    print(fibo(999))
