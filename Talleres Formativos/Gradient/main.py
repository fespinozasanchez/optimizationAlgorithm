import numpy as np


def f(x,function):
    """
    It takes a value of x and a function as arguments and returns the value of the function evaluated at
    x
    
    :param x: the independent variable
    :param function: The function you want to integrate
    :return: The function is being evaluated.
    """
    return eval(function)


def vector_X():
    """
    It returns the vector X
    """
    return np.array([1, 2, 3, 4, 5, 6])


def vector_Delta_X():
    """
    It returns the vector 🔺x
    """
    return np.array([0.001, 0.002, 0.004, 0.006, 0.009, 0.01])


def gradient(x, function, delta_x):
    """
    > The gradient function takes in a value of x, a function, and a delta_x value, and returns the
    gradient of the function at that point
    
    :param x: the point at which we want to evaluate the gradient
    :param function: the function we want to find the minimum of
    :param delta_x: the step size
    :return: The gradient of the function at a given point.
    """
    return (f(x, function) - f(x - delta_x, function)) / delta_x

def main():
    """
    It takes a function, a vector of x values, and a vector of delta x values, and returns a vector of
    gradient values
    """
    x = vector_X()
    function = str(input("Ingrese la funcion: "))
    delta_x = vector_Delta_X()
    vector_Gradient = np.array([gradient(x[i], function, delta_x[i]) for i in range(len(x))])
    print("El vector de gradiente es: ", vector_Gradient)


if __name__ == '__main__':
    main()