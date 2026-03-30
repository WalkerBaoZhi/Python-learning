s=input()
i=0
j=len(s)-1

while s[i]!='-':
    i+=1
while s[j]!='-':
    j-=1
p1=s[0:i]
p2=s[j+1:len(s)]

print (p1,'+',p2,sep='')