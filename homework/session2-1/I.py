pi=float(3.1415927)

while True:
    try:
        r=float(input())
        res = float(4/3 * pi *pow(r,3))
        print("{:.3f}".format(res))
    except EOFError:
        break