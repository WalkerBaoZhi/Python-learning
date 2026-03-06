import math

a,b,c=map(float,input().split(','))
res = float(math.sqrt(a*a+b*b+c*c))
print("{:.2f}".format(res))