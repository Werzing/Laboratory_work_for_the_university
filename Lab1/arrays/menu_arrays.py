from task9_before_last_min import before_last_min
from task21_after_first_max import after_first_max
from task33_alternate_signs import check_alternating_signs
from task45_sum_in_interval import sum_in_interval
from task57_count_greater_than_sum_prev import count_greater_than_sum_prev

def main():
    print("1 – перед последним мин")
    print("2 – после первого макс")
    print("3 – чередование знаков")
    print("4 – сумма в интервале")
    print("5 – больше суммы предыдущих")
    print("6 - выход")
    ch = input("Выберите: ")

    if ch=="6":
        exit()

    stroka = input("Введите числа через пробел: ")
    arr = list(map(int, stroka.split()))
    if ch == '1':
        print(before_last_min(arr))
    elif ch == '2':
        print(after_first_max(arr))
    elif ch == '3':
        print(check_alternating_signs(arr))
    elif ch == '4':
        a = int(input("a = "))
        b = int(input("b = "))
        print(sum_in_interval(arr, a, b))
    elif ch == '5':
        print(count_greater_than_sum_prev(arr))
    else:
        print("Неверный выбор ")

if __name__ == '__main__':
    main()