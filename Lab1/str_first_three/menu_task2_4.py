from task3_shuffle_word import shuffle_words
from task8_even_length_words_count import count_even_length_words
from task16_russian_flag import russian_flag_sort

def main():
    while True:
        print("1 – перемешать слова")
        print("2 – слова с чётной длиной")
        print("3 – сортировка цветов")
        print("4 - выход")
        v = input("Выберите номер: ")
        if v == '1':
            s = input("Строка: ")
            print(shuffle_words(s))
        elif v == '2':
            s = input("Строка: ")
            print(count_even_length_words(s))
        elif v == '3':
            a = input("Цвета через пробел: ").split()
            print(russian_flag_sort(a))
        elif v=="4":
            break
        else:
            print("Неверный выбор")

if __name__ == '__main__':
    main()