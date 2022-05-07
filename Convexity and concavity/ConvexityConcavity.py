import matplotlib.pyplot as plt
import numpy as np


def f(x, str):
    """
    It takes a number and a string as input, and returns the result of evaluating the string as a Python
    expression

    :param x: the independent variable
    :param str: the string to be evaluated
    :return: the result of the evaluation of the string.
    """
    return eval(str)


def verify(x_a, x_b, lamb, fStr):
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
        left_side = f((Lambda*x_a+(1-Lambda)*x_b), fStr)
        right_side = Lambda * f((x_a), fStr) + (1-Lambda)*f((x_b), fStr)
        if left_side >= right_side:
            return 'concave'
        if left_side < right_side:
            return 'convex'
        return 'Not determined'

def points(f,g,x_a,x_b,lamb):
    isVerify = verify(x_a, x_b, lamb, g)
    x = [i for i in np.arange(-4, 4, 0.1)]
    y = [f((i), g) for i in x]
    xExp = [i for i in np.arange(x_a, x_b, 0.1)]
    yExp = [f((lamb*i+(1-lamb)*i), g) for i in xExp]
    xInter = np.linspace(x_a, x_b, 2)
    yInter = np.interp(xInter, xExp, yExp)
    return [x,y,xExp,yExp,xInter,yInter,isVerify]


def graph(Points):
    x,y,xExp,yExp,xInter,yInter,isVerify = Points
    plt.title('Convexity and concavity')
    plt.plot(x, y, color="black", label="f(x)")
    plt.plot(xExp, yExp, color="blue", label="f(λ*x_a+(1-λ)*x_b)\n" +
             'This Function is ' + isVerify)
    plt.plot(xInter, yInter, color='red', label='Interpolation')
    plt.legend()
    plt.grid()
    plt.show()


def main():
    """
    It takes in three inputs, x_a, x_b, and lambda, and then it verifies that the inputs are valid, and
    then it graphs the function
    """
    x_a = float(input("x_a: "))
    x_b = float(input("x_b: "))
    lamb = float(input("lambda[0,1]: "))
    function = str(input("function: "))
    points = points(f, function, x_a, x_b, lamb)
    graph(points)


if __name__ == '__main__':
    main()
