import sympy
from sympy import*

import numpy as np

coord_x = float(input("(x): "))
coord_y = float(input("(y): "))

def get_Point(x,y):
    """
    It takes a string of comma separated numbers and returns a list of the numbers
    
    :param points: The points parameter is a string of comma-separated coord. pairs.
    x and y values should be separated by a comma. For example,
    points = (10,3)
    :return: A list of the points
    """
    return  Matrix([[x], [y]])


print(get_Point(coord_x,coord_y))


def get_Epsilon():
    return np.finfo(float).eps