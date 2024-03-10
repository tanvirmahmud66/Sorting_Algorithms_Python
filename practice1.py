def selection(arr):
    n = len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini], arr[i]


def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        current = arr[i]
        while arr[i-1]>current and i>0:
            arr[i-1], arr[i] = arr[i],arr[i-1]
            i -= 1




arr = [3,2,65,23,66,34,77,22,8,7,4,2,1]
print("Unsorted Array: ",arr)
# selection(arr)
# bubble(arr)
# insertion(arr)
print("Sorted Array: ",arr)