from math import factorial as fac

n=int(input())
sum=0

for i in range (1,n+1):
    sum+=fac(i)

print(sum)