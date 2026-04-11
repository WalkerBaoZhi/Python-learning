n = int(input().strip())

a, b = 0, 1
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    for _ in range(3, n + 1):
        a, b = b, a + b
    print(b)
