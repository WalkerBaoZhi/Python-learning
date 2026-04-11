from sys import stdin

for id in stdin:
    wi=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    s=0
    for i in range(0,17):
        s+=int(id[i])*wi[i]
    y=s%11
    search={
        0:'1',
        1:'0',
        2:'X',
        3:'9',
        4:'8',
        5:'7',
        6:'6',
        7:'5',
        8:'4',
        9:'3',
        10:'2'
    }
    if search[y]==id[17]:
        print('Y')
    else:
        print('N')