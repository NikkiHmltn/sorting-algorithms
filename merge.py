def merge_sorted(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    right = merge_sorted(right)
    left = merge_sorted(left)

    return merge(left, right)

def merge(a, b):
    sorted = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sorted.append(a[i])
            i += 1
        else: 
            sorted.append(b[j])   
            j += 1
    while i < len(a):
        sorted.append(a[i])
        i += 1
    while j < len(b):
        sorted.append(b[j])
        j += 1

    return sorted


array = [3, 6, 1, 6, 4, 78, 44, 11, 20, 22]
print(merge_sorted(array))