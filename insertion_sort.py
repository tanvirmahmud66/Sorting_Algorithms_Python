def insertion(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1


arr = [2,34,23,56,62,32,63,21]
print("Unsorted Array: ",arr)
insertion(arr)
print("Sorted Array: ",arr)