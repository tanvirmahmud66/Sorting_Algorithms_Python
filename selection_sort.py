def Selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini] = arr[mini],arr[i]


arr = [34,25,62,4,6,2,1,67,23]
print("Unsorted Array: ",arr)
Selection_sort(arr)
print("Sorted Array: ",arr)

# time complexity = O(n^2)

