import sys
from math import factorial

import matplotlib.pyplot as plt
import numpy as np

PLOT_RESOLUTION = 1000


def compute_error(x, series_len):
    return np.abs(x**(series_len+1) / factorial(series_len+1))


def sin_approx(x, series_len: int) -> tuple:
    result = 0.0

    for i in range(series_len):
        result = result + (-1)**i * (x**(2*i+1) / factorial(2*i+1))

    return result, compute_error(x, series_len)


def cos_approx(x, series_len: int) -> tuple:
    result = 0.0

    for i in range(series_len):
        result = result + (-1)**i * x**(2*i) / factorial(2*i)

    return result, compute_error(x, series_len)


def main():
    while True:
        try:
            series_len = int(input("Series length: "))
            if series_len < 1:
                raise ValueError
            break
        except ValueError:
            print("Illegal statement, enter again")

    # try:
    #     series_len = int(sys.argv[1])
    #     if series_len < 1:
    #         raise ValueError
    # except ValueError:
    #     print("Number needs to be a positive integer.")
    #     return 1
    # except IndexError:
    #     print("At least 1 program argument needed")
    #     return 1

    x_list = np.linspace(-10, 10, num=PLOT_RESOLUTION)

    sa = sin_approx(x_list, series_len)
    ca = cos_approx(x_list, series_len)

    fig, axs = plt.subplots(2, constrained_layout=True)

    axs[0].set_ylim(-5, 5)
    axs[1].set_ylim(-5, 5)

    axs[0].set_title(f"Approximation and error for sin(x) of order {series_len}")
    axs[1].set_title(f"Approximation and error for cos(x) of order {series_len}")

    axs[0].grid()
    axs[1].grid()

    # plt.plot(x_list, np.vectorize(math.sin)(x_list))
    axs[0].plot(x_list, sa[0], label="sinus approximation")
    axs[1].plot(x_list, ca[0], label="cosine approximation")

    axs[0].plot(x_list, sa[1], label="max approximation error")
    axs[1].plot(x_list, ca[1], label="max approximation error")

    axs[0].legend()
    axs[1].legend()
    plt.show()

    usr_input = 0
    print("Type 'x' in an input to exit program")
    while True:
        x = input("Enter x value [or x to exit]: ")

        if x == 'x' or x == 'X':
            return 0

        try:
            x = float(x)
        except ValueError:
            print("Incorrect input.")

        approx = cos_approx(x, series_len)
        print(f"cos(x={x}) ~= {approx[0]}\n error <= {approx[1]}\n")
        approx = sin_approx(x, series_len)
        print(f"sin(x={x}) ~= {approx[0]}\n error <= {approx[1]}\n")


if __name__ == "__main__":
    exit(main())
