from sympy import *
import sympy

def functions(f: str):
    """
    If the input is a function, return it. Otherwise, convert it to a function

    :param f: the function to be integrated
    :type f: str
    :return: The function itself if it is a function, otherwise it is converted to a sympy function.
    """
    return f if isinstance(f, Function) else sympify(f)


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


def main():
    x = Symbol('x')
    y = Symbol('y')
    function = functions(input('Enter a function: '))
    result = derivatives(function,x,y)
    print(result)
    for i in point_type(x,y, result):
         print(i)

 # Booth function
 # (x + 2*y -7 )**2 + (2*x+y-5)**2   [-10, 10]
 # Beale function
 # (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2    [-4.5, 4.5]


if __name__ == '__main__':
    main()
