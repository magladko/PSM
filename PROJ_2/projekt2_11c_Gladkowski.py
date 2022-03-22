import numpy as np
from decimal import Decimal
from os import system


def trapezoidal_rule(fun, a, b, n):
    integral = 0

    dx = (b - a) / n

    for i in range(n):
        fa = a + dx * i
        fb = a + dx * (i + 1)

        integral += (fun(fa) + fun(fb)) / 2 * dx
    return integral


def simpson_integration_modified(my_func, a, b, n):
    # Szerokość pojedynczego przedziału
    delta_x = (b-a)/n
    total = my_func(a) + my_func(b)
    subtotal_sum_1 = 0
    subtotal_sum_2 = 0
    # pierwsza suma, pamiętamy że n = 2N
    for i in range(0, n, 2):
        x = a + i * delta_x
        subtotal_sum_1 += my_func(x)
    # druga suma, pamiętamy że n = 2N
    for i in range(1, n-1, 2):
        x = a + i * delta_x
        subtotal_sum_2 += my_func(x)
    return delta_x * (total + 4 * subtotal_sum_1 + 2 * subtotal_sum_2) / 3


def main():
    print("PROJ_2 @s22411")
    print("Metoda trapezów:")
    for i in range(1, 6):
        integral = trapezoidal_rule(lambda t: np.sqrt(t) * np.sin(t), 0, i*0.2, 100)
        print(f"\tfor x={round(i*0.2,1)}: {round(Decimal(integral),16)}")
    print("\n")

    print("Metoda 1/3 Simpsona")
    for i in range(1, 6):
        integral = simpson_integration_modified(lambda t: np.sqrt(t) * np.sin(t), 0, i*0.2, 100)
        print(f"\tfor x={round(i*0.2,1)}: {round(Decimal(integral),16)}")
    print()
    system("PAUSE")


if __name__ == '__main__':
    main()
