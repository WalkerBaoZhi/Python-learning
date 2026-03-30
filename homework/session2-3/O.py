parts = input().split()

if len(parts) == 3:
    y, mode, brand = parts
else:
    y, mode = parts
    brand = "宝马"

print(f"这是一辆{y}年生产，型号是{mode}的{brand}牌汽车。")
