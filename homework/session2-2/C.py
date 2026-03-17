a,b,c=map(float,input().split())
maxval = a*6-b*5
minval = a*6-c*5

res = (a*6-maxval-minval)/4
print("%5.2f"%res)