n=int(input())

n=pow(n,n)

s=str(n)
len=len(s)

if len>=2:
    print("%s%s"%(s[len-2],s[len-1]))
else:
    print(s[len-1])