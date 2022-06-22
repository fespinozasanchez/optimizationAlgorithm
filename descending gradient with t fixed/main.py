import sympy
from sympy import*
# Modulos con los que trabajaremos
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
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


def get_Gradient(*args: any) -> list:
    """
    > The function `get_Gradient` takes in two arguments, `x` and `y`, and returns the gradient of the
    function `f` with respect to `x` and `y`
    
    :param : $
    :type : any
    :return: A Matrix of the partial derivatives of the function with respect to the variables.
    """
    if len(args) > 0: return Matrix([[diff(args[0], args[1])], [diff(args[0], args[2])]])


def get_Point(points: str) -> list:
    """
    It takes a string of comma separated numbers and returns a matrix of those numbers
    
    :param points: a string of comma-separated numbers ("x,y")
    :type points: str
    :return: A list of lists of floats.
    """
    return Matrix([ [float(point)] for point in points.split(',') ])

def desc_Gradient(point: list, gradient: list, t: float, n: float, *args:any) -> list:
    """
    The function takes in a point, a gradient, a step size, a tolerance, and a list of variables, and
    returns the point at which the gradient is less than the tolerance
    
    :param point: list, gradient: list, t: float, n: float, *args:any
    :type point: list
    :param gradient: the gradient of the function
    :type gradient: list
    :param t: step size
    :type t: float
    :param n: the norm of the gradient vector
    :type n: float
    :param : point is the starting point
    :type : any
    :return: The point at which the gradient is less than n.
    """
    ad = []
    z = []
    gradient_vector = gradient.subs([(args[0], point[0]), (args[1], point[1])]).norm()
    while  gradient_vector >= n:
        gradient_vector = gradient.subs([(args[0], point[0]), (args[1], point[1])]).norm()
        print(gradient_vector)
        delta_x_n = - gradient.subs([(args[0], point[0]), (args[1], point[1])])
        point = point + t * delta_x_n
        ad.append(point)
        z.append(gradient_vector)
    print("Punto Optimo: " , point, "para el ",gradient)
    return ad,z



def main():
    """
    It takes a function, a point, a scalar, and a number, and returns the gradient descent of the
    function at the point with the scalar and number
    """
    funcion = functions(str(input("Ingrese su función: ")))
    punto = get_Point(str(input("Ingrese un Punto (x,y): ")))
    print(punto)
    n = float(input("Ingrese n (eta): "))
    t = float(input("Ingrese escalar t: "))
    x, y = get_Symbols()
    gradient = get_Gradient(funcion, x, y)
    desc, z = desc_Gradient(punto, gradient, t, n, x,y)
    print(desc)
    xl = []
    yl = []
    for e in desc:
        xl.append(e[0])
        yl.append(e[1])
    
    x = np.array([xl])
    y = np.array([yl])
    z = np.array([z])
    fig = plt.figure()
    ax1 = fig.add_subplot(111,projection='3d')
    ax1.plot_wireframe(x, y, z, color='blue')
    ax1.set_title("3D plot")
    ax1.set_xlabel('x-axis')
    ax1.set_ylabel('y-axis')
    ax1.set_zlabel('z-axis')
    plt.show()

# Booth function
# (x + 2*y -7 )**2 + (2*x+y-5)**2   [-10, 10]
# Beale function
# (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2    [-4.5, 4.5]


if __name__ == '__main__':
    main()