import scipy.optimize as sc
import numpy as np
import sympy as sp


# Definiendo variables y funciones simbolicas
A, C, lam    = sp.symbols('A, C, lam', real=True)
f,g,h,lag= sp.symbols('f,g,h,lag', cls=sp.Function)

c_A=1  # usd
c_C=10 # usd
Bi=100 # M
k=1 # M-1

# Funcion a optimizar (simbolica)
f= -A*c_A+c_C*C # Estructura de la funcion 'f'
h=C-k*((A-2*C)**2*(Bi-C))
lag=f+lam*h
#funcion simpy para derivar funciones simbolicas
g=sp.Matrix ([[sp.diff(lag,A)],[sp.diff(lag,C)],[sp.diff(lag,lam)]])
# jacobian necesita el vector de variables simbolicas a las q derivara
jac=g.jacobian ([A,C,lam])

# Traduciendo a numpy argumentos lambdify [[argumento de la funcion]], f  y la funcion simbolica
utilidad=sp.lambdify([[A,C]],f) # de funcion simbolica a funcion python
restriccion=sp.lambdify([[A,C]],h)
F=sp.lambdify([[A,C,lam]],g)
J=sp.lambdify([[A,C,lam]],jac) 


# Implementacion de Newton multivariable
tol=1e-4
xk=np.array([10,2,1])
#print (xk)
Ea=100
k=0
Z= np.linalg.solve(J(xk), F(xk))
#print (Z)

while Ea>tol and k<500:
	Z= np.linalg.solve(J(xk), F(xk)) # argumentos A, B
	#calcular xkmas1 resta, ver vector y matriz
	xk_mas1= xk - Z.flatten() 
	n_xk_mas1= np.linalg.norm(xk_mas1)
	Ea= 100*abs((n_xk_mas1 - np.linalg.norm(xk))/n_xk_mas1)
	xk=xk_mas1
	k+=1


solucion= xk_mas1[0:2]
#print (solucion, k)

