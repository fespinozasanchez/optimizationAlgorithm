from venv import main
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

X = sp.Symbol('x')


def f(x):
    """
    > The function (x)$ is a quadratic function with a leading coefficient of $ and a constant term
    of $
    
    :param x: the variable
    :return: the value of the function f(x)
    """
    return 3*x**2 + 15*x


def Taylor(vetor_x, delta_x, t, list=[]):
    """
    It takes a vector of x values, a vector of delta x values, a value of t, and a list, and returns a
    list of the Taylor series expansion of f(x) at each x value
    
    :param vetor_x: is a list of the initial values of the variables
    :param delta_x: is the vector of the difference between the initial point and the final point
    :param t: is a scalar
    :param list: list of the results of the Taylor expansion
    :return: a list of values.
    """
    for i in range(len(vetor_x)):
        cal = f(vetor_x[i]) + (np.transpose(sp.diff(f(X), X).subs(X, vetor_x[i])) * delta_x[i])
        cal = cal + ((0.5 * np.transpose(delta_x[i]) * sp.diff(f(X), X, 2).subs(X, (vetor_x[i] + t * delta_x[i]))) * delta_x[i])
        list.append(cal)
    return list


def vector_X():
    """
    It returns a list of numbers from -6 to 1, in steps of 0.5
    :return: A list of numbers from -6 to 1 in increments of 0.5
    """
    return [i for i in np.arange(-6,1,0.5)]


def vector_Delta_x(x):
    """
    > It returns an array of 0.01's that is the same length as the input array
    
    :param x: the vector of values of the independent variable
    :return: A vector of length x with all elements equal to 0.01
    """
    return np.array([0.01 for e in range(len(x))])


def fx_eval(x, list=[]):
    """
    It takes a list of numbers, squares each number, adds 6 to each number, and returns a list of the
    results
    
    :param x: the list of variables
    :param list: the list of values to be returned
    :return: A list of the values of the function evaluated at each point in the list x.
    """
    for i in range(len(x)):
        list.append(3 * x[i]**2 + 15*x[i])
    return list


def graph(x, taylor):
    """
    It takes in a list of x values and a list of taylor polynomial values, and plots the original
    function and the taylor polynomial on the same graph
    
    :param x: the x-values to evaluate the function at
    :param taylor: the taylor series approximation of f(x)
    """
    plt.plot(x,fx_eval(x),color="blue",label='Exact Value')
    plt.plot(x,taylor,color="red",label="Taylor")
    plt.legend()
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('Value')
    plt.show()


def main():
    """
    The function main() calls the functions vector_X(), vector_Delta_x(), Taylor(), and graph() to
    create a graph of the Taylor series approximation of the function f(x) = sin(x) with a = 1
    """
    vector_x = vector_X()
    delta_x = vector_Delta_x(vector_x)
    taylor = Taylor(vector_x, delta_x, 1)
    graph(vector_x, taylor)



if __name__ == '__main__':
    main()
