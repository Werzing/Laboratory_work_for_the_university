def find_dates(text):
    months = ["января", "февраля", "марта", "апреля", "мая", "июня",
              "июля", "августа", "сентября", "октября", "ноября", "декабря"]

    for punct in '.,;:!?()"\'':
        text = text.replace(punct, ' ')

    words = text.split()
    found = []
    for i in range(len(words) - 2):
        day = words[i]
        month = words[i + 1]
        year = words[i + 2]

        if (day.isdigit() and 1 <= int(day) <= 31 and
                month in months and
                year.isdigit() and len(year) == 4):
            found.append(f"{day} {month} {year}")

    return found


# Пример использования
text = "В 31 февраля 2007 было событие. Потом 29 февраля 2020, и ещё 30 февраля 2023!"
result = find_dates(text)
for date in result:
    print(date)
