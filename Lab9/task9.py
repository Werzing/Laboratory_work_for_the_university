import csv
from datetime import datetime
from collections import defaultdict

# Словарь для перевода русских названий месяцев в номера
MONTHS = {
    'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4,
    'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8,
    'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12
}

def parse_russian_date(date_str):
    """
    Преобразует строку вида '15 Май 2017  12:41' в объект datetime.
    """
    # Разделяем по пробелам, учитывая возможные двойные пробелы
    parts = date_str.split()
    # Пример: ['15', 'Май', '2017', '12:41']
    day = int(parts[0])
    month_str = parts[1]
    year = int(parts[2])
    time_str = parts[3]
    hour, minute = map(int, time_str.split(':'))
    month = MONTHS[month_str]
    return datetime(year, month, day, hour, minute)

def process_file(filename):
    """
    Читает CSV-файл, возвращает словарь: email -> (first_name, last_name, earliest_success_date)
    """
    # Словарь для хранения информации о слушателях
    # Ключ: email, значение: [фамилия, имя, минимальная дата успешной попытки]
    best_attempt = {}

    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)  # пропускаем заголовок

        for row in reader:
            # Пропускаем строки, которые не содержат данных (например, итоговые)
            if len(row) < 10 or row[5] != 'Завершено':
                continue

            # Извлекаем нужные поля
            last_name = row[0].strip()
            first_name = row[1].strip()
            email = row[4].strip()
            finish_date_str = row[7].strip()
            try:
                score = float(row[9].replace(',', '.'))  # оценка/100.00
            except ValueError:
                continue  # на случай, если оценка не число

            # Успешная попытка: балл >= 60
            if score < 60:
                continue

            # Парсим дату завершения
            try:
                finish_date = parse_russian_date(finish_date_str)
            except:
                # Если не удалось распарсить, пропускаем
                continue

            # Если этот email уже есть, сравниваем даты
            if email not in best_attempt or finish_date < best_attempt[email][2]:
                best_attempt[email] = (last_name, first_name, finish_date)

    # Преобразуем в список кортежей для сортировки
    result = []
    for email, (last, first, date) in best_attempt.items():
        result.append((last, first, date))

    # Сортируем по дате (от самой ранней)
    result.sort(key=lambda x: x[2])
    return result

def main():
    filename = '9 - 2.csv'  # используем файл с оценкой/100
    sorted_list = process_file(filename)

    print("Список слушателей, успешно прошедших тест, в порядке даты выполнения (самая ранняя первая):")
    for last, first, date in sorted_list:
        print(f"{last} {first} – {date.strftime('%d.%m.%Y %H:%M')}")

if __name__ == '__main__':
    main()