from math import pow as p
import numpy as np

def bruteForce(thetaV, deltaXV, list=[]):
    """
    This function applies brute force to find all suboptimal solutions given a restriction and save the points evaluated and its value Z.
    :param thetaV:Refers to the θ value of this problem to evaluate.
    :param deltaXV:Refers to the Δx of this problem to evaluate.
    :param list:Would be the list generated that will contain the points evaluated and its Z value.
    :return: The list generated.
    """
    try:
        for x1 in np.arange(0, 6, deltaXV):
            for x2 in np.arange(0, 6, deltaXV):
                if((x1 + x2) <= 5):
                    evA = 1.20 * x1 + 1.16 * x2 - thetaV *  (2*p(x1, 2) + p(x2, 2)+p((x1+x2), 2))
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
    thetaV = float(input("ThetaV: "))
    deltaXV = float(input("DeltaXV: "))
    list = bruteForce(thetaV, deltaXV)
    print(maxTupla(list))

if __name__ == '__main__':
    main()

