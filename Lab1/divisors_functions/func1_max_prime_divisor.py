def max_prime_divisor(n):
    if n < 2:
        return None
    max_d = 1
    for i in range(2, n+1):
        if n % i == 0:
            # проверка, простое ли i
            prost = True
            for j in range(2, i):
                if i % j == 0:
                    prost = False
                    break
            if prost:
                max_d = i
    return max_d

# Проверка
print(max_prime_divisor(6)) #5
print(max_prime_divisor(49)) #7