def f(s, n):
    if s == "":
        return ""
    n = n % len(s)
    return s[-n:] + s[:-n]

s = input()
n = int(input())
print(f(s, n))
