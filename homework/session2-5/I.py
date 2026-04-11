def F(x, n):
    if n == 1:
        return x / (1 + x)
    return x / (n + F(x, n - 1))

x, n = map(float, input().split())
print(f"{F(x, int(n)):.2f}")
