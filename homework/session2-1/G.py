s=input()
temp = float(s[1:])
if s[0] == 'F':
    res = (temp-32)/1.8
    print("C""{:.2f}".format(res))
else:
    res = temp*1.8+32
    print('F'"{:.2f}".format(res))