import re

def count_letters(word, letters_set):
    """Возвращает количество символов word, входящих в letters_set"""
    return sum(1 for ch in word.lower() if ch in letters_set)

def main():
    # ввод букв
    letters_input = input("Введите искомые буквы (без пробелов): ").strip()
    letters_set = set(letters_input.lower())

    # чтение файла с текстом
    filename = 'text.txt'
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print("Файл text.txt не найден")
        return

    # выделяем слова (только русские буквы)
    words = re.findall(r'[а-яё]+', text.lower(), re.IGNORECASE)

    best_word = None
    best_cnt = -1
    for w in words:
        cnt = count_letters(w, letters_set)
        if cnt > best_cnt:
            best_cnt = cnt
            best_word = w

    if best_word is None:
        print("В тексте нет слов")
    else:
        print(f"Слово с наибольшим количеством указанных букв: {best_word}")
        print(f"Количество вхождений: {best_cnt}")

if __name__ == '__main__':
    main()