def before_last_min(arr):
    if not arr:
        return []
    mn = arr[0]
    for x in arr:
        if x < mn:
            mn = x
    last_idx = -1
    for i in range(len(arr)):
        if arr[i] == mn:
            last_idx = i
    return arr[:last_idx]

# print(before_last_min([3,1,4,1,5]))