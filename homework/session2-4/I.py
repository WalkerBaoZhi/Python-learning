n=float(input())
learn=0

for i in range(0,365):
    if learn==10:
        n*=0.999
        learn=0
    else:
        n*=1.001
        learn+=1
    

print (f"365天后该同学的能力是{n:.6f}")