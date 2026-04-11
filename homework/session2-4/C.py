import random

n=int(input())

random.seed(n)
for i in range (0,10):
    print(f"{random.randint(0,999)}",end='')