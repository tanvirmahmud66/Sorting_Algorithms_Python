def bubble(arr):
    n = len(arr)
    for i in range(n): 
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [23,342,252,646,32342,66,322,342,66323,66233,62223,23,66,32323,66]
print("Unsorted Array: ",arr)
bubble(arr)
print("Sorted Array: ",arr)

# time complexity = n^2