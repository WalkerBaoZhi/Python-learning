freqDirt = eval(input())
s = input().strip()
p = s.split()

for c in p:
    if c in freqDirt:
        freqDirt[c]+=1
    else:
        freqDirt[c]=1

print(freqDirt)