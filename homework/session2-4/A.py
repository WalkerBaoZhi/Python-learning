while True:
    try:
        s=input()
        dic=set()
        res=[]
        for ch in s:
            if ch not in dic:
                dic.add(ch)
                res.append(ch)
        print("".join(res))
    except EOFError:
        break