import sympy as sp
from math import sqrt

def f(x, str):
    """
    It takes a string and evaluates it as a Python expression
    :param str: The string to evaluate
    """
    return eval(str)


def derive(x_symbol, fx):
    """
    > It takes a string representing a function of x, and returns a string representing the derivative
    of that function

    :param x_symbol: The variable you want to differentiate with respect to
    :param fx: the function to be differentiated
    :return: The derivative of the function fx with respect to x_symbol.
    """
    return str(sp.diff(fx, x_symbol))


def algorithm_1(fx, x):
    """
    It takes a function and a value, and returns the derivative of the function at that value
    :param fx: The function to be derived
    :param x: The value of x that you want to use in the function
    """
    x_symbol = sp.Symbol('x')
    derivation = derive(x_symbol, fx)
    return eval(str(derivation))


def algorithm_2(dfx, x, dx, f, str):
    """
    It takes in a function, a value, a step size, and a string, and returns the difference between the
    derivative of the function at the value and the limit of the function at the value
    :param dfx: the derivative of the function f(x)
    :param x: the value of x that you want to find the derivative at
    :param dx: delta x value
    :param f: function
    :param str: string of the function
    :return: The difference between the actual derivative and the derivative calculated by the
    algorithm.
    """
    lim = (f(x+dx,str)- f(x,str))/dx
    difference = abs(dfx - lim)
    return [lim, difference]
   


def main():
    x = int(input("Ingrese el valor de x: "))
    fx = str(input("Ingrese la funcion: "))
    dx_value = sqrt(2.22e-16) * x

    derivate = algorithm_1(fx, x)
    lim, difference = algorithm_2(derivate, x, dx_value, f, fx)
    print("La derivada de la funcion es: ", derivate, "\ny la derivada calculada por la definicion de limites es  es: ", lim)
    print("La diferencia entre  derivada de f(x) - el limite f(x + dx)-f(x) / dx = ", difference)


if __name__ == '__main__':
    main()
