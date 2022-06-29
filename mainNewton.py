import sympy
from sympy import*
import numpy as np
# Modulos con los que trabajaremos
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
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
    It returns a list of two symbols, `x`
    :return: A list of two symbols, x
    """
    return Symbol('x'),Symbol('y')

def get_Derivative2(f: sympy.Expr, n: int) -> sympy.Expr:
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
    x,y = get_Symbols()

    return sympy.diff(f, x, n),sympy.diff(f, y, n)


def get_Gradient2(f: sympy.Expr, n: int) -> sympy.Expr:
    """
    It takes a function, a variable, a number of derivatives, and a point, and returns the gradient of
    the function at that point

    :param f: sympy.Expr = the function you want to find the gradient of
    :type f: sympy.Expr
    :param X: sympy.Symbol = The variable you want to differentiate with respect to
    :type X: sympy.Symbol
    :param n: The number of variables in the function
    :type n: int
    :param x: the value of x
    :type x: int
    :return: A matrix with the value of the derivative of f with respect to X at x.
    """
    x,y = get_Symbols()
    dx,dy=get_Derivative2(f, n)
    return Matrix([[eval(str(dx))]]),Matrix([[eval(str(dy))]])


def hessian(f: sympy.Expr) -> sympy.Expr:
    x, y = get_Symbols()
    dx = diff(f, x)
    dxx=diff(dx, x)
    dxy=diff(dx,y)
    dy = diff(f, y)
    dyy = diff(dy, y)
    dyx=diff(dy,x)
    hessian=np.array([[dxx,dxy],[dyx,dyy]],dtype=np.int64)
    hi=np.linalg.inv(hessian)
    return hi

def get_Epsilon()->float:
    """
    The function returns the smallest positive number that can be represented by the float data type
    :return: The smallest positive number that can be represented in the float data type.
    """
    return np.finfo(float).eps

def Newton_method2(f: sympy.Expr, x_n:float,y_n:float,e:float )->sympy.Expr:
    '''
    :param f: refers to the simpy function
    :param x_n: refers to the x point to evaluate
    :return:
    '''
    x,y = get_Symbols()
    hi = hessian(f)
    grx_n, gry_n = get_Gradient2(funcion, 1)
    points = np.array([[x_n], [y_n]])
    current_Gradient = Matrix([grx_n.evalf(subs={x: x_n, y: y_n}), gry_n.evalf(subs={x: x_n, y: y_n})],dtype=np.int64)
    current_coords =np.array( points - np.dot(hi, current_Gradient))
    x_A=[]
    y_A=[]
    z_A=[]
    x_A.append(x_n)
    y_A.append(y_n)
    z_A.append(Matrix([grx_n.evalf(subs={x: x_n, y: y_n}), gry_n.evalf(subs={x: x_n, y: y_n})]).norm())
   #ITERABLE#
    while ((np.linalg.norm(np.array(current_coords-points, dtype=np.int64))) >= e):
        points = np.array([[x_n], [y_n]])
        current_Gradient = Matrix([grx_n.evalf(subs={x: x_n, y: y_n}), gry_n.evalf(subs={x: x_n, y: y_n})],dtype=np.int64)
        current_coords =points - np.dot(hi, current_Gradient)
        x_n = float(current_coords[0])
        y_n = float(current_coords[1])
        x_A.append(x_n)
        y_A.append(y_n)
        z_A.append(Matrix([grx_n.evalf(subs={x: x_n, y: y_n}), gry_n.evalf(subs={x: x_n, y: y_n})]).norm())
    return x_A,y_A,z_A


def grafB(xl,yl, z):


    x = np.array([xl])
    y = np.array([yl])
    z = np.array([z])
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.plot_wireframe(x, y, z, color='blue')
    ax1.set_title("Método de Newton")
    ax1.set_xlabel('x-axis')
    ax1.set_ylabel('y-axis')
    ax1.set_zlabel('z-axis')
    plt.show()


# Booth function
# (x + 2*y -7 )**2 + (2*x+y-5)**2  [-10, 10]
# Beale function
# (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2    [-4.5, 4.5]
x, y = get_Symbols()
e=get_Epsilon()
funcion = functions(str(input("Ingrese su funcion: ")))
x_n = float(input("Ingrese x: "))
y_n = float(input("Ingrese y: "))
xa,ya,za=Newton_method2(funcion,x_n,y_n,e)
print(xa,ya,za)
grafB(xa,ya,za)




