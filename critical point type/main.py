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


def derivatives(f,x,y):
    dx = diff(f, x)
    dy = diff(f, y)
    dx2 = diff(dx, x)
    dy2 = diff(dy, y)
    fxy = diff(dx, y)
    sol = solve((dx, dy), (x, y))
    dev=[dx,dy,dx2,dy2,fxy,sol]
    return dev

def main():
    x = Symbol('x')
    y = Symbol('y')
    f = input('Enter a function: ')
    function = functions(f)
    print(derivatives(function,x,y))


if __name__ == '__main__':
    main()
