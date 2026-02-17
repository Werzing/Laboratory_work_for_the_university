def count_greater_than_sum_prev(arr):
    if len(arr) <= 1:
        return 0
    count = 0
    sum_prev = 0
    for i in range(1, len(arr)):
        current = arr[i]
        if current > sum_prev:
            count += 1
        sum_prev += current
    return count

if __name__ == '__main__':
    print(count_greater_than_sum_prev([1, 3, 2, 7]))
    print(count_greater_than_sum_prev([5, 1, 2]))
    print(count_greater_than_sum_prev([1, 2, 4, 8]))
    print(count_greater_than_sum_prev([]))
    print(count_greater_than_sum_prev([10]))
    print(count_greater_than_sum_prev([0, 1, 2, 4]))
