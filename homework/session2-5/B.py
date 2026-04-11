n_str = input().strip()

# 检查是否为正整数
if not n_str.isdigit():
    print("ERROR")
else:
    n = int(n_str)
    if n <= 0:
        print("ERROR")
    else:
        seq = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
            seq.append(n)
        # 第一行：序列
        print(" ".join(str(x) for x in seq))
        # 第二行：运算次数 = 步数 = 序列长度 - 1
        print(len(seq) - 1)
