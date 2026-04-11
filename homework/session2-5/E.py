def calc(a, n):
    s = 0
    t = 0
    for _ in range(n):
        t = t * 10 + a
        s += t
    return s

a, n = map(int, input().split())
print(calc(a, n))
