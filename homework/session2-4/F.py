N = int(input())

for j in range(1, N):
    for g in range(1, N):
        # 九头鸟的头数 = 9
        # 头的方程：j + g + 9n = N
        # => n = (N - j - g) / 9
        if (N - j - g) % 9 != 0:
            continue
        n = (N - j - g) // 9
        if n <= 0:
            continue

        # 脚的方程：2j + 4g + 2n = N
        if 2*j + 4*g + 2*n == N:
            print(f"鸡的数量是{j}")
            print(f"狗的数量是{g}")
            print(f"九头鸟的数量是{n}")
