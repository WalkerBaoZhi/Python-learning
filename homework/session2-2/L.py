n=int(input())
a=n//100
b=(n-a*100)//10
c=(n-a*100-b*10)

if n==(pow(a,3)+pow(b,3)+pow(c,3)):
    print('1')
else:
    print('0')