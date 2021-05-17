import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return x**3

def f(x):
    return np.sin(x)


def main():
    x = np.linspace(-10, 10, num=1000)

    fo_o_g = f(g(x))

    plt.grid()
    plt.plot(x, fo_o_g)
    plt.show()

if __name__ == '__main__':
    main()