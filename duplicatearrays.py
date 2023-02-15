arr=array('i',[])
N= int(input("enter the length of array:"))
for i in range(N):
     a=int(input("enter the number:"))
     arr.append(a)
print(arr)

for i in range(len(arr)):
     for j in range(i+1,len(arr)):
         if (arr[i]==arr[j]):
             print(arr[i])

