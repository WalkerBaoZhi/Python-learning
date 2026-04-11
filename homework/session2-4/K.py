s=""
a= int(input())

while a//2!=0:
    s+=str(a%2)
    a//=2
s+=str(a%2)
print(s[::-1])