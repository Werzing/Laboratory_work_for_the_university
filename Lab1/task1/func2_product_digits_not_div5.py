def product_digits_not_div5(n):
    n = abs(n)
    product = 1
    has_valid_digit = False

    for digit_char in str(n):
        digit = int(digit_char)
        if digit not in (0, 5):  # не делится на 5
            product *= digit
            has_valid_digit = True

    return product if has_valid_digit else 0


# Тестирование
print(product_digits_not_div5(13579))  # 189
print(product_digits_not_div5(505))  # 0
print(product_digits_not_div5(0))  # 0
print(product_digits_not_div5(-246))  # 48 (2*4*6)
