import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    s = float(line)
    if s>=90 and s<=100:
       print('A')
    elif s>=80 and s<90:
        print('B')
    elif s>=70 and s<80:
        print('C')
    elif s>=60 and s<70:
        print('D')
    elif s>=0 and s<60:
        print('E')
    else:
        print('Score is error!')