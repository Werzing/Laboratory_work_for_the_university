from task3_count_cyrillic import count_cyrillic
from task8_lower_latin_used import used_lower_latin
from task16_min_integer_in_string import min_integer_in_string

def main():
    while True:
        print("Выберите задачу:")
        print("1 - количество русских символов")
        print("2 - все строчные латинские буквы")
        print("3 - минимальное целое число")
        print("4 - выход")

        choice = input("Ваш выбор: ")
        if choice == '4':
            print("Выход")
            break

        s = input("Введите строку: ")
        if choice == '1':
            print("Русских символов:", count_cyrillic(s))
        elif choice == '2':
            print("Используемые строчные латинские:", used_lower_latin(s))
        elif choice == '3':
            print("Минимальное целое число:", min_integer_in_string(s))
        else:
            print("Неверный выбор")

if __name__ == '__main__':
    main()