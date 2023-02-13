a=[0,3,0,2,0]

def pushzeroatend(arr):
    numzero=0

    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i] ,arr[numzero] = arr[numzero] ,arr[i]

            numzero+=1
    return arr

pushzeroatend(a)

print(a)
