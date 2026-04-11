n=int(input())
a,b=2,1
s=0

for i in range(n):
   s+=a/b
   a,b = a+b,a

print(f"{s:.3f}")