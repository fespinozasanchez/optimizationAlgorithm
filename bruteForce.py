from math import pow as p
import numpy as np

x = x1 = x2 = 0
thetaV = 0.0
deltaXV = 0.0

def functionObjective(x1, x2, thetaV):
    return 1.20 * x1 + 1.16 * x2 - thetaV *  (2*p(x1, 2) + p(x2, 2)+p((x1+x2), 2))
    
def bruteForce(thetaV, deltaXV, list=[]):
    try:
        for x1 in np.arange(0, 6, deltaXV):
            for x2 in np.arange(0, 6, deltaXV):
                if((x1 + x2) <= 5):
                    evA = functionObjective(x1,x2,thetaV)
                x = (x1, x2)
                list.append((x, evA))
    except Exception as e:
        print(e)
    return list


def maxTupla(arr):
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

