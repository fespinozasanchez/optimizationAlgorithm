from math import pow as p
import numpy as np

# def objectiveFunction(x1, x2, thetaV):
#     """

#     :param x1:Expect the x1 value for the objective function.
#     :param x2:Expect the x2 value for the objective function.
#     :param thetaV:Expect the θ value for the objective function , is a constant that represents the risk .
#     :return:The function evaluated ,Z Value.
#     """
#     return 1.20 * x1 + 1.16 * x2 - thetaV *  (2*p(x1, 2) + p(x2, 2)+p((x1+x2), 2))

def objectiveFunction2(functionObejctive):
    return functionObejctive

def bruteForce(*args, list=[]):
    """
    This function applies brute force to find all suboptimal solutions given a restriction and save the points evaluated and its value Z.
    :param thetaV:Refers to the θ value of this problem to evaluate.
    :param deltaXV:Refers to the Δx of this problem to evaluate.
    :param list:Would be the list generated that will contain the points evaluated and its Z value.
    :return: The list generated.
    """
    try:
        for x1 in np.arange(0, 6, args[3]):
            for x2 in np.arange(0, 6, args[3]):
                if((x1 + x2) <= 5):
                    evA = objectiveFunction2(args[0] * x1 + args[2] * x2 - args[2] *  (2*p(x1, 2) + p(x2, 2)+p((x1+x2), 2)))
                x = (x1, x2)
                list.append((x, evA))
    except Exception as e:
        print(e)
    return list


def maxTupla(arr):
    """
    This function find the max value of a given array in the position 1, being this case the Z of the function.
    :param arr: An array is expected  that contains tuples of  x,y points evaluated in the f(x,y) function.
    :return:Returns the max value of the function and its points (x,y).
    """
    if len(arr)!=0: 
        return max(arr, key=lambda x: x[1])
    return "Empty Array"

def main():    
    x = x1 = x2 = 0
    thetaV = 0.0
    deltaXV = 0.0
    A = 1.20
    B = 1.16
    thetaV = float(input("ThetaV: "))
    deltaXV = float(input("DeltaXV: "))
    list = bruteForce(A,B,thetaV, deltaXV)
    print(maxTupla(list))

if __name__ == '__main__':
    main()

