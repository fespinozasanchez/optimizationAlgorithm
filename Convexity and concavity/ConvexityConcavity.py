
from cProfile import label

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    """
    > The function `f` takes a number `x` and returns the value of the quadratic function (x) = x^2 +
    2x + 1$
    
    :param x: the variable
    :return: the value of the function f(x)
    """
    return x**2+2*x+1


def verify(x_a, x_b, lamb):
    """
    If the left side of the inequality is greater than the right side, then the function is concave. If
    the left side is less than the right side, then the function is convex. If neither of these are
    true, then the function is neither concave nor convex
    
    :param x_a: the first point
    :param x_b: the point where the tangent line intersects the x-axis
    :param lamb: the value of lambda
    :return: the string 'No determine'
    """
    for Lambda in np.arange(lamb, 1, 0.1):
        left_side = f(Lambda*x_a+(1-Lambda)*x_b)
        right_side = Lambda * f(x_a) + (1-Lambda)*f(x_b)
        if left_side >= right_side:
            return 'concave'
        if left_side < right_side:
            return 'convex'
        return 'No determine'


def graph(f, x_a, x_b, lamb, verify):
    """
    It takes a function, two points, a lambda value, and a string, and plots the function, the
    interpolation between the two points, and the string
    
    :param f: the function to be plotted
    :param x_a: the first point
    :param x_b: the second point
    :param lamb: the value of lambda
    :param verify: the verification of the convexity/concavity
    """
    x = [i for i in np.arange(-10, 10, 0.1)]
    y = [f(i) for i in x]
    x_a = [i for i in np.arange(x_a, x_b, 0.1)]
    y_a = [f(lamb*i+(1-lamb)*i) for i in x_a]

    yinterp = np.interp(x, x_a, y_a)

    plt.title('Convexity and concavity')

    plt.plot(x, y, color="black", label="f(x)")
    plt.plot(x_a, y_a, color="blue", label="f(λ*x_a+(1-λ)*x_b)\n"+verify)
    plt.plot(x,yinterp, color='red',label='interpolation')
    plt.legend()
    plt.show()


def main():
    """
    It takes in three inputs, x_a, x_b, and lambda, and then it verifies that the inputs are valid, and
    then it graphs the function
    """
    x_a = float(input("x_a: "))
    x_b = float(input("x_b: "))
    lamb = float(input("lambda[0,1]: "))
    isVerify = verify(x_a, x_b, lamb)
    graph(f, x_a, x_b, lamb, isVerify)


if __name__ == '__main__':
    main()
