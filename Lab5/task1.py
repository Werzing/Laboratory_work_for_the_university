import re

def is_html_image_tag(s):
    """Возвращает True, если строка является корректным HTML-тегом изображения."""
    pattern = r'^<img\s+[^>]*>$'
    return re.fullmatch(pattern, s) is not None

def get_html_image_tag(s):
    """Возвращает строку, если она корректна, иначе выбрасывает ValueError."""
    if is_html_image_tag(s):
        return s
    else:
        raise ValueError("Некорректный код изображения HTML")

# Демонстрация работы
if __name__ == "__main__":
    test_strings = [
        '<img src="image.jpg">',
        '<img src="image.jpg" alt="picture">',
        '<img src="image.jpg" />',
        '<img src="image.jpg" / >',
        '<img src="image.jpg"',
        '<img>',
        ' <img src="a">',      # ведущий пробел – не подходит
        '<img src="image.jpg" alt=\'picture\'>',  # одинарные кавычки
    ]
    print("Тестовые строки:")
    for s in test_strings:
        print(f"'{s}': {is_html_image_tag(s)}")
        try:
            print(f"   Результат get: {get_html_image_tag(s)}")
        except ValueError as e:
            print(f"   Ошибка: {e}")

    # Ввод пользователя
    user_input = input("\nВведите строку для проверки: ")
    if is_html_image_tag(user_input):
        print("✅ Это корректный код изображения HTML")
    else:
        print("❌ Это не корректный код изображения HTML")