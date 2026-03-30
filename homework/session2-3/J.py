s=input()
leng = len(s)

for i in range(0,leng):
    if i%2==0:
        print(s[i],i,sep='',end='')