s=input().strip()
dic = {}

for i in s:
    if ord('0')<=ord(i)<=ord('9'):
        print("ERROR")
        exit()
    elif i in dic:
        dic[i]+=1
    else:
        dic[i]=1

print(dic)
print(len(s))

p1 = list(dic.keys())
p2 = list(dic.values())
leng = len(p1)
count = 0

for i in range(leng):
    if p2[i]==1:
        print(f"{p1[i]}",end='')
        count+=len(p1[i])
    else:
        print(f"{p1[i]}{p2[i]}",end='')
        count+=(len(p1[i])+len(str(p2[i])))

print(f"\n{count}")