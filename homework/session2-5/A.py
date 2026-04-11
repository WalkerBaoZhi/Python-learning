from random import seed, randint

def gen_code():
    s = ""
    for _ in range(10):
        t = randint(1, 5)  # 1/5 digit, 2/5 upper, 2/5 lower
        if t == 1:
            s += str(randint(0, 9))
        elif t == 2 or t == 3:
            s += chr(randint(ord('A'), ord('Z')))
        else:  # 4 or 5
            s += chr(randint(ord('a'), ord('z')))
    return s

n = int(input().strip())
seed(n)

codes = set()
while len(codes) < 5:
    c = gen_code()
    if c not in codes:
        codes.add(c)

for c in codes:
    print(c)
