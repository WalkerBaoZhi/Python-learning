from sympy import isprime

a,b=map(int,input().split())

for i in range(a,b+1):
    if isprime(i):
        print(i,end=' ')