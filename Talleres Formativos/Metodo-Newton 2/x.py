import numpy as np

#Metodo de Newton-Raphson Multivariable
def newtonRaphsonMV(F,J,x,imax=10000,tol=1e-8):
    cumple=False
    k=0
    while (not cumple and k<imax):
        # print("Hola:",J(x),'FOLA:', -F(x))
        deltax=np.linalg.solve(J(x), -F(x))
        x = x + deltax
        print('iteracion:{}-> {}'.\
              format(k,x))
        cumple=np.linalg.norm(F(x))<=tol
        k+=1
    if k<imax:
        return x
    else:
        print('La funcion no converge')

# Vector de Funciones
def f(x):
    return np.array([2+(x[0]-2)**2+(x[1]-1)**2 ,  9*x[0]-(x[1]-1)**2 ])
#Matriz Jacobiana
def j(x):
    return np.array([[2*x[0]-4, 2*x[1]-2],\
                     [9, -2*x[1] + 2] ])

def main():
    # valores iniciales
    x0=np.array([-20,20])
    # Llamada al algoritmo
    raiz=newtonRaphsonMV(f,j,x0)
    print('f({})={}'.format(raiz,f(raiz)))
    
if __name__ == "__main__": main()