import sympy as sp 

def f(str):
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
    print(f"La derivada de la funcion {fx} es: " + derivation)
    print(f"La funcion con datos ya remplazados es: {eval(str(derivation))}")


def algorithm_2():
    pass

def main():
    dx = float(input("Ingrese el valor de dx: "))
    x = int(input("Ingrese el valor de x: "))
    fx = str(input("Ingrese la funcion: "))
    algorithm_1(fx,x)





if __name__ == '__main__':
    main()
