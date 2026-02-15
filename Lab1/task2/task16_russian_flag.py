def russian_flag_sort(colors):
    # сортировка пузырьком
    n = len(colors)
    for i in range(n-1):
        for j in range(n-i-1):
            # определяем вес цвета
            def get_weight(c):
                if c == 'белый':
                    return 0
                elif c == 'синий':
                    return 1
                else:
                    return 2
            if get_weight(colors[j]) > get_weight(colors[j+1]):
                colors[j], colors[j+1] = colors[j+1], colors[j]
    return colors

arr = ["синий", "красный", "белый", "красный", "белый", "синий"]
# print(russian_flag_sort(arr))