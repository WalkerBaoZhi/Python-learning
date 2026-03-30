a,b,c=map(int,input().split())

if (a==b or a==c or b==c) and not (a==b==c):
    print("Yes",end='')
else:
    print("No",end='')