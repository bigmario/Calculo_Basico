from sympy import limit, Symbol

x=Symbol('x')

y = 1/x

limite_izquierda = limit(y, x, 0, '-')
limite_derecha = limit(y, x, 0, '+')

print(limite_izquierda)
print(limite_derecha)