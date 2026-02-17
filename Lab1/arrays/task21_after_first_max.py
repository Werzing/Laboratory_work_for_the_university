def after_first_max(arr):
    if not arr:
        return []
    mx = arr[0]
    for x in arr:
        if x > mx:
            mx = x
    first_idx = -1
    for i in range(len(arr)):
        if arr[i] == mx:
            first_idx = i
            break
    return arr[first_idx+1:]

# print(after_first_max([3,5,1,5,2]))