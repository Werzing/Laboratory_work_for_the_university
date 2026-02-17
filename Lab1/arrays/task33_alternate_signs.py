def check_alternating_signs(arr):

    if len(arr) <= 1:
        return True

    for i in range(len(arr) - 1):
        current = arr[i]
        next_val = arr[i + 1]

        if current == 0 or next_val == 0:
            return False

        if current * next_val > 0:
            return False

    return True


if __name__ == '__main__':
    print(check_alternating_signs([1, -2, 3, -4]))      # True (чередуется)
    print(check_alternating_signs([1, -2, 0, -4]))     # False (есть ноль)
    print(check_alternating_signs([-1, 2, -3, 4]))     # True (чередуется)
    print(check_alternating_signs([1, 2, 3]))          # False (все положительные)
    print(check_alternating_signs([-1, -2, -3]))       # False (все отрицательные)
    print(check_alternating_signs([]))                  # True (тривиально)
    print(check_alternating_signs([5]))                # True (тривиально)
    print(check_alternating_signs([0, 1]))            # False (ноль нарушает)
