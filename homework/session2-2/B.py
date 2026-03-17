n = int(input())
sum = 0

if n%3==0:
    sum+=3
if n%5==0:
    sum+=5
if n%7==0:
    sum+=7

if sum==15:
    print('1')
if sum==8:
    print('2')
if sum==10:
    print('3')
if sum==12:
    print('4')
if sum==3:
    print('5')
if sum==5:
    print('6')
if sum==7:
    print('7')
if sum==0:
    print('8')