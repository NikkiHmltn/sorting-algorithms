def partition(arr, start, end):
    i = (start - 1)
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[end] = arr[j], arr[i + 1]
    return (i + 1)

def quick(arr, start, end):
    if len(arr) <= 1:
        return arr
    if start < end :
        index = partition(arr, start, end)
        quick(arr, start, index - 1)
        quick(arr, index + 1, end)

array = [11, 6, 3, 7, 8, 4, 9]
n = len(array)
print(quick(array, 0, n - 1))