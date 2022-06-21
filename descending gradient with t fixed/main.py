import sympy
from sympy import*
import numpy as np


def functions(f: str):
    """
    If the input is a function, return it. Otherwise, convert it to a function

    :param f: the function to be integrated
    :type f: str
    :return: The function itself if it is a function, otherwise it is converted to a sympy function.
    """
    return f if isinstance(f, Function) else sympify(f)



def get_Symbols()->list:
    """
    It returns a list of two symbols, `x` and `y`
    :return: A list of two symbols, x and y.
    """
    return Symbol('x'), Symbol('y')


def get_Point(points: str) -> list:
    """
    It takes a string of comma separated numbers and returns a matrix of those numbers
    
    :param points: a string of comma-separated numbers ("x,y")
    :type points: str
    :return: A list of lists of floats.
    """
    return Matrix([ [float(point)] for point in points.split(',') ])

def get_Derivative(f: sympy.Expr, x: sympy.Symbol, n: int) -> sympy.Expr:
    """
    It takes a function, a variable, and a number, and returns the nth derivative of the function with
    respect to the variable

    :param f: sympy.Expr - the function to take the derivative of
    :type f: sympy.Expr
    :param x: the variable you want to differentiate with respect to
    :type x: sympy.Symbol
    :param n: the number of times you want to differentiate the function
    :type n: int
    :return: The nth derivative of f with respect to x.
    """
    return sympy.diff(f, x, n)






def get_Epsilon()->float:
    """
    The function returns the smallest positive number that can be represented by the float data type
    :return: The smallest positive number that can be represented in the float data type.
    """
    return np.finfo(float).eps



def Newton_method(f: sympy.Expr, x: sympy.Symbol, t: float, n: int, gradiente:sympy.matrices.dense.MutableDenseMatrix)->sympy.Expr:


    return t*gradiente


def main():
    """
    It takes a function, a point, a scalar, and a number, and returns the gradient descent of the
    function at the point with the scalar and number
    """
    e = get_Epsilon()
    x, y = get_Symbols()
    funcion = functions(str(input("Ingrese su función: ")))
    punto = get_Point(str(input("Ingrese un Punto (x,y): ")))
    t = float(input("Ingrese escalar t: "))
    gradiente = get_Gradient(funcion,x,2)
    print(type(gradiente))
    