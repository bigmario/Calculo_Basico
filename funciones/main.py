import codeacademy.funcion_polinomial as poli
import codeacademy.funcion_cuadratica as cuad
import codeacademy.funcion_lineal as lin
import codeacademy.trascendentes as tras

import matplotlib.pyplot as plt
import numpy as np


def run():
    N=100 #Tamaño del dominio (numero de puntos en X)

    x=np.linspace(-10, 10, num=N)
    # x=np.linspace(0.01, 100, num=N) #para la funcion logaritmica, x > 0

    e=np.e

    m=2 #pendiente
    b=1 #corte en y

    # y1=lin.f(m,x,b)
    # y2=poli.f(x)
    # y3=cuad.f(x)
    # y4=tras.seno(x)
    # y5=tras.coseno(x)
    # y6=tras.tangente(x)
    # y7=tras.exponencial(e, x)
    # y8=tras.logaritmo(x)
    y9=tras.h(x)

    plt.grid()
    # plt.plot(x, y1) #lineal
    # plt.plot(x, y2) #Polinomial
    # plt.plot(x, y3) #Cuadratica
    # plt.plot(x, y4) #Seno
    # plt.plot(x, y5) #Coseno
    # plt.plot(x, y6) #Tangente
    # plt.plot(x, y7) #Exponencial
    # plt.plot(x, y8) #Logaritmo
    y9=plt.plot(x, y9)
    
    # plt.xlim(-100, 100)
    # plt.ylim(-10, 10)
    # plt.axhline(y=0, color='r')
    # plt.axvline(x=0, color='r')
    
    plt.xlabel('Dominio')
    plt.ylabel('Rango')
    
    plt.show()


if __name__ == '__main__':
    print('*'*50)
    print('PRACTICA DEL CURSO DE CALCULO BASICO')
    run()