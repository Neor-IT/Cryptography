from math import fabs, sqrt
from random import randint


def first(m, a):
    return a % m


def second(m, a, b):
    return a ** b % m


def third(m, a, b, x):
    return a * x == b % m


def is_prime(n):  # допоміжна функція для перевірки числа на те, чи просте воно
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True


def fourth(a=0, b=100):  # генератор простих чисел у діапазоні від a до b
    num = 0
    while is_prime(num) is False:
        num = randint(a, b)
    return num


def main():
    m = fabs(-10)
    print(first(m, 5))
    print(second(m, 5, 6))
    print(third(m=m, a=4, b=8, x=2))
    print(fourth())


if __name__ == '__main__':
    main()
