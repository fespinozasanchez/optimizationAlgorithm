import sympy
from sympy import*
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
def bruteForce(rango1,rango2, deltaXV, f, list=[]):
    """
    This function applies brute force to find all suboptimal solutions given a restriction and save the points evaluated and its value Z.
    :param thetaV:Refers to the θ value of this problem to evaluate.
    :param deltaXV:Refers to the Δx of this problem to evaluate.
    :param list:Would be the list generated that will contain the points evaluated and its Z value.
    :return: The list generated.
    """
    xl = []
    yl = []
    z =  []
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
    return list,xl,yl,z


def maxTupla(arr):
    """
    This function find the max value of a given array in the position 1, being this case the Z of the function.
    :param arr: An array is expected  that contains tuples of  x,y points evaluated in the f(x,y) function.
    :return:Returns the max value of the function and its points (x,y).
    """
    if len(arr)!=0: 
        return max(arr, key=lambda x: x[1])
    return "Empty Array"

def minTupla(arr):
    """
    This function find the max value of a given array in the position 1, being this case the Z of the function.
    :param arr: An array is expected  that contains tuples of  x,y points evaluated in the f(x,y) function.
    :return:Returns the max value of the function and its points (x,y).
    """
    if len(arr)!=0: 
        return min(arr, key=lambda x: x[1])
    return "Empty Array"

def graficar3d(puntoMaximo,puntoMinimo,x,y,z):
    fig = plt.figure()
    ax1 = fig.add_subplot(111,projection='3d')
    ax1.plot_wireframe(x, y, z, color='blue')
    ax1.scatter(puntoMaximo[0][0], puntoMaximo[0][1], puntoMaximo[1], color='green', marker='o')
    ax1.scatter(puntoMinimo[0][0], puntoMinimo[0][1], puntoMinimo[1], color='red', marker='o')
    ax1.scatter(1, 3, 0, color='black', marker='o')
    ax1.set_title("3D plot")
    ax1.set_xlabel('x-axis')
    ax1.set_ylabel('y-axis')
    ax1.set_zlabel('z-axis')
    plt.show()
############################################################################## FUERZA BRUTA ####################################################################################

############################################################################## PUNTO CRITICO ####################################################################################

def derivatives(f,x,y):
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
    derivate2_x,derivate2_y, derivate_x_y, points = result
    response = []
    if len(points) <= 2 :
            dic = points
            print(dic)
            h_x = derivate2_x.evalf(subs=dic) * derivate2_y.evalf(subs=dic) - derivate_x_y.evalf(subs=dic) **2
            if h_x < 0: response.append(f"H(x)= {h_x} para {points} por lo tanto es: un punto silla")
            if (h_x > 0 and (derivate2_x.evalf(subs=dic) < 0 or derivate2_y.evalf(subs=dic)<0) ):response.append( f"H(x)= {h_x} para {points} por lo tanto es: un máximo local.")
            if (h_x > 0 and (derivate2_x.evalf(subs=dic) > 0 or derivate2_y.evalf(subs=dic)>0) ):response.append( f"H(x)= {h_x} para {points} por lo tanto es: un mínimo local.")
            if (h_x)==0: response.append(f"No existe información suficiente sobre el punto {points}.")
    else:
        for point in points:
            if (type(point[1]) is not sympy.core.add.Add):
                dic = {x:point[0],y:point[1]}
                print(dic)
                h_x = derivate2_x.evalf(subs=dic) * derivate2_y.evalf(subs=dic) - derivate_x_y.evalf(subs=dic) **2
                if h_x < 0: response.append(f"H(x)= {h_x} para {point} por lo tanto es: un punto silla")
                if (h_x > 0 and (derivate2_x.evalf(subs=dic) < 0 or derivate2_y.evalf(subs=dic)<0) ):response.append( f"H(x)= {h_x} para {point} por lo tanto es: un máximo local.")
                if (h_x > 0 and (derivate2_x.evalf(subs=dic) > 0 or derivate2_y.evalf(subs=dic)>0) ):response.append( f"H(x)= {h_x} para {point} por lo tanto es: un mínimo local.")
                if (h_x)==0: response.append(f"No existe información suficiente sobre el punto {point}.")
    return response
############################################################################## PUNTO CRITICO ####################################################################################

def main1(function):
    rango1 = float(input("rango1: "))
    rango2 = float(input("rango2: "))
    deltaXV = float(input("DeltaXV: "))
    Points, x,y,z = bruteForce(rango1,rango2, deltaXV, function)
    puntoMaximo = maxTupla(Points)
    puntoMinimo = minTupla(Points)
    print("Maximo:",puntoMaximo)
    print("Minimo:",puntoMinimo)
    x = np.array([x])
    y = np.array([y])
    z = np.array([z])
    graficar3d(puntoMaximo,puntoMinimo,x,y,z)


def main2(function):
    x = Symbol('x')
    y = Symbol('y')
    result = derivatives(function,x,y)
    print(result)
    for i in point_type(x,y, result):
         print(i)



 # Booth function
 # (x + 2*y -7 )**2 + (2*x+y-5)**2   [-10, 10]
 # Beale function
 # (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2    [-4.5, 4.5]


if __name__ == '__main__':
    function = functions((input("Ingresa la función: ")))
    print("\nFuerza Bruta\n")
    main1(function)
    print("\nPunto Critico\n")
    main2(function)