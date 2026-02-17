def sum_in_interval(arr, a, b):
    s = 0
    for x in arr:
        if a <= x <= b:
            s += x
    return s

# print(sum_in_interval([1,5,3,8,2], 2, 5))