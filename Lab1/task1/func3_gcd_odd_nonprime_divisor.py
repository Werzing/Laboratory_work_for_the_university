def gcd_odd_nonprime_and_product(n):
    # все нечётные делители n
    nechet_deliteli = []
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0 and i != 1:
            nechet_deliteli.append(i)

    # не простые ("а золотые" ^_^)
    neprostye = []
    for d in nechet_deliteli:
        prostoe = True
        if d < 2:
            prostoe = False
        else:
            for j in range(2, d):
                if d % j == 0:
                    prostoe = False
                    break
        if not prostoe:
            neprostye.append(d)

    # Если нет делителей, то 0
    if len(neprostye) == 0:
        return 0


    max_del = max(neprostye)

    # произведение цифр числа
    chislo_stroka = str(abs(n))
    proizvedenie = 1
    for simvol in chislo_stroka:
        proizvedenie = proizvedenie * int(simvol)


    if proizvedenie == 0:
        return 0

    # алгоритмом Евклида
    a = max_del
    b = proizvedenie
    while b != 0:
        a, b = b, a % b
    return a

# Тест
print(gcd_odd_nonprime_and_product(45))   #5
print(gcd_odd_nonprime_and_product(49))   #1
print(gcd_odd_nonprime_and_product(30))   #0