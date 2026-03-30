id=input()

yyyy=id[6:10]
mm=id[10:12]
dd=id[12:14]
sex=id[16]

print("出生：",yyyy,"年",mm,"月",dd,"日",sep='')

if ord(sex)%2!=0:
    print("性别：男")
else:
    print("性别：女")