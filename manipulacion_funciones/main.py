import matplotlib.pyplot as plt
import numpy as np

import codeacademy.funciones as fn


def run():
    N=1000 #Tamaño del dominio (numero de puntos en X)

    c=10

    x=np.linspace(-10, 10, num=N)
    # x=np.linspace(0.01, 100, num=N) #para la funcion logaritmica, x > 0

    e=np.e

    m=2 #pendiente
    b=50 #desplazamiento en y


    y=fn.f(x)-b

    plt.grid()
    
    # plt.xlim(-100, 100)
    # plt.ylim(-10, 10)
    plt.axhline(y=0, color='r')
    plt.axvline(x=0, color='r')
    
    plt.xlabel('Dominio')
    plt.ylabel('Rango')

    plt.plot(x, y)
    
    plt.show()


if __name__ == '__main__':
    print('*'*50)
    print('PRACTICA DEL CURSO DE CALCULO BASICO')
    run()