import math as m


a=float(input())
b=float(input())

x = (-b + m.sqrt(2*a*m.sin(m.radians(60))*m.cos(m.radians(60)))) / (2*a)

print(x)