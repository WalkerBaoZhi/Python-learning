while True:
    try:
        a=float(input())
        break
    except ValueError:
        print("请输入有效的数字！")
        exit()

while True:
    try:
        b=float(input())
        break
    except ValueError:
        print("请输入有效的数字！")
        exit()

if b==0:
    print("除数不能为零，请重新输入！")
else:
    print(a/b)