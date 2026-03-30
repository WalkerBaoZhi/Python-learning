s=input()
r=""

for i in s:
    if i>='a' and i<='z':
        r+=chr(ord(i)-32)
    else:
        r+=i     

print(r)