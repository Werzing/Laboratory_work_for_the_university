from criterion3_freq_diff import sort_strings_by_criterion3
from criterion5 import sort_by_criterion5
from criterion9 import sort_by_criterion9
from criterion11 import sort_by_criterion11

def main():
    print("Выберите критерий сортировки строк:")
    print("1 – разница частоты самого частого символа")
    print("2 – квадратичное отклонение частоты")
    print("3 – отклонение max ASCII от среднего зеркальных пар")
    print("4 – отклонение от max средней тройки первой строки")
    print("5 - выход")
    choice = input("Ваш выбор (1/2/3/4/5): ")

    if choice =="5":
        exit()

    print("Введите строки (одну за другой, пустая строка – конец):")
    lines = []
    while True:
        s = input()
        if s == "":
            break
        lines.append(s)

    if not lines:
        print("Нет строк для сортировки.")
        return

    if choice == '1':
        result = sort_strings_by_criterion3(lines)
    elif choice == '2':
        result = sort_by_criterion5(lines)
    elif choice == '3':
        result = sort_by_criterion9(lines)
    elif choice == '4':
        result = sort_by_criterion11(lines)
    else:
        print("Неверный выбор.")
        return

    print("\nОтсортированный список:")
    for s in result:
        print(s)

if __name__ == '__main__':
    main()