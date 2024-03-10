def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


arr = [2,35,23,64,77,36,43,62,23,65,44,33,23,20]
print("Unsorted Array: ",arr)
bubble(arr)
print("Sorted Array: ",arr)


# time complexity = O(n^2)