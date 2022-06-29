import sympy
from sympy import *
import numpy as np


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


############################################################################## FUERZA BRUTA ####################################################################################
def bruteForce(rango1, rango2, deltaXV, f, list=[]):
    """
    This function applies brute force to find all suboptimal solutions given a restriction and save the points evaluated and its value Z.
    :param thetaV:Refers to the θ value of this problem to evaluate.
    :param deltaXV:Refers to the Δx of this problem to evaluate.
    :param list:Would be the list generated that will contain the points evaluated and its Z value.
    :return: The list generated.
    """
    xl = []
    yl = []
    z = []
    try:
        for x in np.arange(rango1, rango2, deltaXV):
            for y in np.arange(rango1, rango2, deltaXV):
                if((x + y) <= 5):
                    evA = eval(str(f))
                xs = (x, y)
                xl.append(x)
                yl.append(y)
                z.append(evA)
                list.append((xs, evA))
    except Exception as e:
        print(e)
    return list, xl, yl, z


def maxTupla(arr):
    """
    This function find the max value of a given array in the position 1, being this case the Z of the function.
    :param arr: An array is expected  that contains tuples of  x,y points evaluated in the f(x,y) function.
    :return:Returns the max value of the function and its points (x,y).
    """
    if len(arr) != 0:
        return max(arr, key=lambda x: x[1])
    return "Empty Array"


def minTupla(arr):
    """
    This function find the max value of a given array in the position 1, being this case the Z of the function.
    :param arr: An array is expected  that contains tuples of  x,y points evaluated in the f(x,y) function.
    :return:Returns the max value of the function and its points (x,y).
    """
    if len(arr) != 0:
        return min(arr, key=lambda x: x[1])
    return "Empty Array"


def graficar3d(puntoMaximo, puntoMinimo, x, y, z):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.plot_wireframe(x, y, z, color='blue')
    ax1.scatter(puntoMaximo[0][0], puntoMaximo[0][1],
                puntoMaximo[1], color='green', marker='o')
    ax1.scatter(puntoMinimo[0][0], puntoMinimo[0][1],
                puntoMinimo[1], color='red', marker='o')
    ax1.scatter(1, 3, 0, color='black', marker='o')
    ax1.set_title("Fuerza Bruta")
    ax1.set_xlabel('x-axis')
    ax1.set_ylabel('y-axis')
    ax1.set_zlabel('z-axis')
    plt.show()
############################################################################## FUERZA BRUTA ####################################################################################

############################################################################## PUNTO CRITICO ####################################################################################


def derivatives(f, x, y):
    """
    It takes a function (x,y)$ and returns the partial derivatives of $ with respect to $ and $,
    the second partial derivatives of $ with respect to $ and $, and the solutions to the system
    of equations $\frac{\partial f}{\partial x} = 0$ and $\frac{\partial f}{\partial y} = 0$

    :param f: the function
    :param x: the x-coordinate of the point
    :param y: the function
    :return: The first two elements are the second derivatives of f with respect to x and y. The third
    element is the second derivative of f with respect to x and y. The fourth element is the solution to
    the system of equations.
    """
    dx = diff(f, x)
    dy = diff(f, y)
    sol = solve((dx, dy), (x, y))
    return [diff(dx, x), diff(dy, y), diff(dx, y), sol]


def point_type(x, y, result):
    derivate2_x, derivate2_y, derivate_x_y, points = result
    response = []
    if len(points) <= 2:
        dic = points
        print(dic)
        h_x = derivate2_x.evalf(
            subs=dic) * derivate2_y.evalf(subs=dic) - derivate_x_y.evalf(subs=dic) ** 2
        if h_x < 0:
            response.append(
                f"H(x)= {h_x} para {points} por lo tanto es: un punto silla")
        if (h_x > 0 and (derivate2_x.evalf(subs=dic) < 0 or derivate2_y.evalf(subs=dic) < 0)):
            response.append(
                f"H(x)= {h_x} para {points} por lo tanto es: un máximo local.")
        if (h_x > 0 and (derivate2_x.evalf(subs=dic) > 0 or derivate2_y.evalf(subs=dic) > 0)):
            response.append(
                f"H(x)= {h_x} para {points} por lo tanto es: un mínimo local.")
        if (h_x) == 0:
            response.append(
                f"No existe información suficiente sobre el punto {points}.")
    else:
        for point in points:
            if (type(point[1]) is not sympy.core.add.Add):
                dic = {x: point[0], y: point[1]}
                print(dic)
                h_x = derivate2_x.evalf(
                    subs=dic) * derivate2_y.evalf(subs=dic) - derivate_x_y.evalf(subs=dic) ** 2
                if h_x < 0:
                    response.append(
                        f"H(x)= {h_x} para {point} por lo tanto es: un punto silla")
                if (h_x > 0 and (derivate2_x.evalf(subs=dic) < 0 or derivate2_y.evalf(subs=dic) < 0)):
                    response.append(
                        f"H(x)= {h_x} para {point} por lo tanto es: un máximo local.")
                if (h_x > 0 and (derivate2_x.evalf(subs=dic) > 0 or derivate2_y.evalf(subs=dic) > 0)):
                    response.append(
                        f"H(x)= {h_x} para {point} por lo tanto es: un mínimo local.")
                if (h_x) == 0:
                    response.append(
                        f"No existe información suficiente sobre el punto {point}.")
    return response
############################################################################## PUNTO CRITICO ####################################################################################


############################################################################## DESCENDENTE CON T FIJO ####################################################################################
def get_Symbols() -> list:
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
    if len(args) > 0:
        return Matrix([[diff(args[0], args[1])], [diff(args[0], args[2])]])


def get_Point(points: str) -> list:
    """
    It takes a string of comma separated numbers and returns a matrix of those numbers

    :param points: a string of comma-separated numbers ("x,y")
    :type points: str
    :return: A list of lists of floats.
    """
    return Matrix([[float(point)] for point in points.split(',')])

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

    
def grafD(desc,z):
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
    ax1.set_title("Gradiente Descendente con t Fijo")
    ax1.set_xlabel('x-axis')
    ax1.set_ylabel('y-axis')
    ax1.set_zlabel('z-axis')
    plt.show()
############################################################################## DESCENDENTE CON T FIJO ####################################################################################


############################################################################## DESCENDENTE  Barzilai-Borwein ####################################################################################
def derivatives2(f,x,y):
    """
    It takes a function (x,y)  and returns the partial derivative of x,y 
    
    :param f: the function
    :param x: the x-coordinate of the point
    :param y: the function
    :return: The first two elements are the second derivatives of f with respect to x and y,
    respectively. 
    """
    dx = diff(f, x)
    dy = diff(f, y)
    return Matrix([[dx],[dy]])

def barz_borw(tV,xV,yV,gradientV,etaV,x,y):
    '''
    This function take for parameters a scale value, (x,y) coordinates, its gradient, an eta value and the x,y symbols.
    :param tV: refers to the t value (scale value).
    :param xV: refers to x coordinate value.
    :param yV: refers to y coordinate value.
    :param gradientV: refers to the gradient of the function f(x,y).
    :param etaV: refers to eta value.
    :param x: refers to x symbol.
    :param y: refers to y symbol.
    :param oGr : refers to the old gradient or the first gradient calculated before reasignating t.
    :param nGr : refers to the new gradient value after reasignating t.
    :param dx : referst to the Δ𝑥𝑛:=−∇𝑓(𝑥𝑛) value.
    :param lwP :refers to the lowest part of the equation (||∇𝑓(𝑥𝑛)−∇𝑓(𝑥𝑛−1)||2)
    :return:   Return the  Barzilai-Borwein algorithm value  on the given data.
    '''
    cords=Matrix([[float(xV)],[float(yV)]])
    ad = []
    z = []
    while(float(gradientV.subs([(x,cords[0]),(y,cords[1])]).norm())>=etaV):
        oGr= gradientV.subs([(x,cords[0]),(y,cords[1])])
        dx= -tV * oGr
        z.append(float(gradientV.subs([(x,cords[0]),(y,cords[1])]).norm()))
        cords=cords+dx
        nGr=gradientV.subs([(x,cords[0]),(y,cords[1])])
        lwP = nGr - oGr
        oGr = nGr
        tV = dx.dot(lwP) / lwP.dot(lwP)
        ad.append(cords)
        
    return cords,ad,z

def grafB(desc,z):
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
    ax1.set_title("Gradiente Descendente con Barzilai-Borwein")
    ax1.set_xlabel('x-axis')
    ax1.set_ylabel('y-axis')
    ax1.set_zlabel('z-axis')
    plt.show()
        

############################################################################## DESCENDENTE  Barzilai-Borwein ####################################################################################

def main1(function):
    rango1 = float(input("rango1: "))
    rango2 = float(input("rango2: "))
    deltaXV = float(input("DeltaXV: "))
    Points, x, y, z = bruteForce(rango1, rango2, deltaXV, function)
    puntoMaximo = maxTupla(Points)
    puntoMinimo = minTupla(Points)
    print("Maximo:", puntoMaximo)
    print("Minimo:", puntoMinimo)
    x = np.array([x])
    y = np.array([y])
    z = np.array([z])
    graficar3d(puntoMaximo, puntoMinimo, x, y, z)


def main2(function):
    x = Symbol('x')
    y = Symbol('y')
    result = derivatives(function, x, y)
    print(result)
    for i in point_type(x, y, result):
        print(i)

def main3(function):
    """
    It takes a function, a point, a scalar, and a number, and returns the gradient descent of the
    function at the point with the scalar and number
    """
    punto = get_Point(str(input("Ingrese un Punto (x,y): ")))
    print(punto)
    n = float(input("Ingrese n (eta): "))
    t = float(input("Ingrese escalar t: "))
    x, y = get_Symbols()
    gradient = get_Gradient(function, x, y)
    desc, z = desc_Gradient(punto, gradient, t, n, x,y)
    print("Puntos Descendientes: ",desc)
    grafD(desc,z)


def main4(function):
    x = Symbol('x')
    y = Symbol('y')
    tV = float(input('Enter a t value between 0-1: '))
    eV =float( input('Enter a eta value: '))
    xV= float(input('Enter the x  value: '))
    yV= float(input('Enter the y  value: '))
    gradientV = derivatives2(function,x,y)
    cords,desc,z=barz_borw(tV,xV,yV,gradientV,eV,x,y)

    print(cords)
    print(desc)
    grafB(desc,z)







# Booth function
# (x + 2*y -7 )**2 + (2*x+y-5)**2   [-10, 10] ->2,2 n=0.0001, t= 0.2
# Beale function
# (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2    [-4.5, 4.5]


if __name__ == '__main__':
    function = functions((input("Ingresa la función: ")))
    print("\nFuerza Bruta\n")
    main1(function)
    print("\nPunto Critico\n")
    main2(function)
    print("\nGradiente Descendiente: t Fijo\n")
    main3(function)
    print("\nGradiente Descendiente: Barzilai-Borwein\n")
    main4(function)