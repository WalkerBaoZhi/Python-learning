dic1 = {'Tom':21,'Bob':18,'Jack':23,'Ana':20}
dic2 = {'李雷':21,'韩梅梅':18,'小明':23,'小红':20}

n=int(input())
n=min(n,len(dic1))

dic1 = sorted(dic1.keys())[:n]
dic2 = sorted(dic2.items(),key=lambda x:x[1])[:n]


print(dic1)
print(dic2)