def sort_strings_by_length():
    lines = []
    while True:
        s = input("Введите строку (Enter для завершения): ")

        if s == "":
            break
        lines.append(s)
    lines.sort(key=len)
    print("Отсортировано по длине:")
    for line in lines:
        print(line)

if __name__ == '__main__':
    sort_strings_by_length()