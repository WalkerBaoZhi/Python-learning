s=input()

word=digit=other=space=0

for c in s:
    if 'a'<=c<='z' or 'A'<=c<='Z':
        word+=1
    elif '0'<=c<='9':
        digit+=1
    elif c==' ':
        space+=1
    else:
        other+=1

print(f"英文字母{word}个，数字{digit}个\n其他字符{other}个，空格{space}个")