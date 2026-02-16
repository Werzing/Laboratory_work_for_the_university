def sort_strings_by_word_count():
    lines = []
    print("Вводите строки (чтобы закончить — нажмите Enter):")

    while True:
        s = input()
        if s == "":
            break
        lines.append(s)

    n = len(lines)
    for i in range(n):
        for j in range(0, n - i - 1):
            words_in_current = len(lines[j].split())
            words_in_next = len(lines[j + 1].split())

            if words_in_current > words_in_next:
                lines[j], lines[j + 1] = lines[j + 1], lines[j]

    print("\nОтсортировано по количеству слов (от меньшего к большему):")
    for line in lines:
        word_count = len(line.split())
        print(f"{word_count} слов: {line}")

sort_strings_by_word_count()
