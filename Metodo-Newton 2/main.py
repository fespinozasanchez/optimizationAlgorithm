import numpy as np
from sympy import *
import sympy


def functions(f1: str, f2: str) -> list:
    """
    If the input is a function, return the function. If the input is a string, return the string as a
    sympy function

    :param f1: str, f2:str, x:Symbol, y:Symbol
    :type f1: str
    :param f2: the function that you want to find the derivative of
    :type f2: str
    :param x: the independent variable
    :type x: Symbol
    :param y: the function to be solved for
    :type y: Symbol
    :return: an array of the two functions if they are both functions. If they are not both functions,
    it is returning the two functions as sympy functions.
    """
    return Matrix([f1, f2]) if isinstance((f1, f2), Function) else Matrix([sympify(f1), sympify(f2)])


def gradient(functions: list, x: Symbol, y: Symbol) -> list:
    """
    > The function `gradient` takes a list of functions and returns a list of the partial derivatives of
    those functions

    :param functions: list of functions
    :type functions: list
    :return: The gradient of the function.
    """
    return Matrix([[diff(functions[0], x), diff(functions[0], y)], [diff(functions[1], x), diff(functions[1], y)] ]) 


def get_Symbols() -> list:
    """
    It returns a list of two symbols, `x` and `y`
    :return: A list of two symbols, x and y.
    """
    return Symbol('x'), Symbol('y')


def get_Points():
    return Matrix([input('ingresa el Punto X0: '),
                   input('Ingresa el Punto Y0: ')])


# Metodo de Newton-Raphson Multivariable
def newtonRaphsonMV(function: list, jacobiana: list, points, x, y, tol=1e-8):
    print('j:',jacobiana.evalf(subs={x: points[0], y: points[1]}))
    print('f:',-function.evalf(subs={x: points[0], y: points[1]}))
    cumple = False
    k = 0
    matrix_j = jacobiana.evalf(subs={x: points[0], y: points[1]})
    matrix_f = function.evalf(subs={x: points[0], y: points[1]})
    while (not cumple ):

        jj =  np.array([[matrix_j[0],matrix_j[1]],[matrix_j[2],matrix_j[3]]],dtype=np.int64)
        ff = np.array([[matrix_f[0]],[matrix_f[1]]],dtype=np.int64)
        print('J: ',jj,'F(x):',ff)
        deltax = np.linalg.solve(jj, ff)
        points = points + deltax
        print('iteracion:{}-> {}'.format(k, points))
        cumple = np.linalg.norm(ff) <= tol
        k+=1
    if cumple:
        return points
    else:
        print('La funcion no converge')



def main():
    f1 = input("Ingresa la función f1: ")
    f2 = input("Ingresa la función f2: ")
    function = functions(f1,f2)
    x, y = get_Symbols()
    points = get_Points()
    _matrix_Jacobiana = gradient(functions(f1, f2), x, y)
    print(_matrix_Jacobiana)

    # # Llamada al algoritmo
    raiz = newtonRaphsonMV(function, _matrix_Jacobiana, points,x,y)
    print('f({})'.format(raiz))


if __name__ == "__main__":
    main()
