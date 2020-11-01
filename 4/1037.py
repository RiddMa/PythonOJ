def main():
    n, s = map(int, input().split())
    max_predict_t = 0
    for i in range(n):
        xi, vi = map(int, input().split())
        if xi >= s:
            # 开始就在终点前，不需要考虑
            continue
        else:
            t_predict = (s - xi) / vi
            if t_predict > max_predict_t:
                max_predict_t = t_predict
    print(f"{max_predict_t:.2f}")


main()
