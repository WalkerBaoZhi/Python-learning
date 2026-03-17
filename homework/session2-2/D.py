arr = list(map(int,input().split()))
arr.sort(reverse=True)

for i in range(len(arr)):
    if i != len(arr)-1:
        print(arr[i],end=" ")
    else:
        print(arr[i])