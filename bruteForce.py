import  math
import numpy as np
x=x1=x2=0
theta=0.0
deltaX =0.0
xyArray =[]
def isEmpty(arr):
    return len(arr) == 0

def bruteForce(thetaV, deltaXV):
    for x1 in np.arange(0, 6, deltaX):
        for x2 in np.arange(0, 6, deltaX):
            if((x1 + x2) <=5):
                objF= 1.20 * x1 + 1.16 * x2 - theta * (2*math.pow(x1,2)+ math.pow(x2,2)+math.pow((x1+x2),2))
            x=(x1,x2)
            xyArray.append((x,objF))