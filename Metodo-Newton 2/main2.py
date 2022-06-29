import autograd.numpy as np
import autograd
# Modulos con los que trabajaremos
import matplotlib.pyplot as plt
import numpy as np

def newton(f, x0, tol=1.48e-08, maxiter=150):
    g = autograd.grad(f)
    h = autograd.hessian(f)
    x = x0
    xy = []
    for _ in range(maxiter):
        delta = np.linalg.solve(h(x), -g(x))
        x = x + delta
        xy.append(x)
        if np.linalg.norm(delta) < tol:
            break

    return x,xy

def f(x):
    return  (1.5-x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0] * (x[1]**2))**2 + (2.625 - x[0] + x[0]*(x[1]**3))**2


def graficar3d(points, x, y, z):
    print(points)
    x = np.array([x])
    y = np.array([y])
    z = np.array([z])
    print( z[0][len(z)-1])
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.plot_wireframe(x, y, z, color='blue')
    ax1.scatter(points[0], points[1], z[0][len(z)-1], color='green', marker='o')
    ax1.set_title("Metodo Newton")
    ax1.set_xlabel('x-axis')
    ax1.set_ylabel('y-axis')
    ax1.set_zlabel('z-axis')
    plt.show()

def main():
    x0 = np.array([5.0, 0.5])
    points,xy = newton(f, x0)
    x = []
    y = []
    z = []
    for i in xy:
        x.append(i[0])
        y.append(i[1])    
        z.append(f(i))

    graficar3d(points,x,y,z)


#(x + 2*y -7 )**2 + (2*x+y-5)**2  (x[0] +  2*x[1]-7)**2 + (2*x[0] + x[1]-5)**2
# (1.5 - x + x*y)**2 + (2.25 - x + x*(y**2))**2 + (2.625 - x + x*(y**3))**2   (1.5-x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0] * (x[1]**2))**2 + (2.625 - x[0] + x[0]*(x[1]**3))**2

if __name__ == '__main__':
    main()