#print Second largest element from unsorted array
def array(a,n):
    largest=0
    slargest=-1
    for i in range(n):
        if(a[i]>largest):
            slargest=largest
            largest=a[i]
    print(slargest)

arr1 = [2, 3, 4, 5,5,1,0]
print("The given array is ", str(arr1))
n = len(arr1)
array(arr1,n)

arr = [9, 9, 9]
print("The given array is ", str(arr))
n = len(arr)
array(arr, n)
