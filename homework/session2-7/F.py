dict1 = {'赵广辉': '13299887777', '特朗普': '814666888', '普京': '522888666', '吴京': '13999887777'}
s=input()
num=input()

if s in dict1:
    dict1[s] = num
else:
    print("数据不存在")

for i in dict1:
    print(f"{i}:{dict1[i]}")