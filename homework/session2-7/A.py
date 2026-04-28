n = int(input())

a=[]

for _ in range(n):
    name,age=input().split()
    age=int(age)
    a.append({"name":name,"age":age})

s1 = sorted(a,key=lambda x: x["age"])
s2 = sorted(a,key=lambda x: x["name"])

print(f"{s1}\n{s2}")