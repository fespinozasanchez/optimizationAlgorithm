from sympy import *


def functions(f: str):
    """
    If the input is a function, return it. Otherwise, convert it to a function

    :param f: the function to be integrated
    :type f: str
    :return: The function itself if it is a function, otherwise it is converted to a sympy function.
    """
    return f if isinstance(f, Function) else sympify(f)


def point_type(x, y, solution):
    for point in solution:
        pass


def main():
    x = Symbol('x')
    y = Symbol('y')
    f = input('Enter a function: ')
    function = functions(f)
    derivate_x = function.diff(x)
    derivate_y = function.diff(y)
    solution = solve((derivate_x, derivate_y), [x, y])
    print(solution)


if __name__ == '__main__':
    main()
