import numpy as np

#optmizacion manual B=A*Z

def g (X): # B
	x= X[0,0]
	y= X[1,0]
	return np.array([[0.15-0.1*(x-10)-0.007*y],[0.22-0.032*y-0.007*(x-10)]])

def J (X): # A
	x= X[0,0]
	y= X[1,0]
	return np.array([[-0.1,-0.007],[-0.007,-0.032]])

Ea=100
tol=1e-4
k=0
Xk=np.array([[1],[2]])

while Ea>tol:
	Z=np.linalg.solve(J(Xk),g(Xk))
	Xk_mas1=Xk-Z
	# el error se calcula con la norma,ya que estamos trabajando con vectores.
	n_Xk=np.linalg.norm(Xk)
	n_Xk_mas1=np.linalg.norm(Xk_mas1)
	Ea=abs((n_Xk_mas1-n_Xk)/n_Xk_mas1)*100
	Xk=Xk_mas1 
	k+=1


# reemplazando la raiz en la funcion para conocer el maximo y comprobar que g(xk raiz) la pendiente es cero.
def f (X):
	x= X[0,0]
	y= X[1,0]
	return 7.7+0.15*(x-10)+0.22*y-0.05*(x-10)**2-0.016*y**2-0.007*(x-10)*y

print (f(Xk), ".....", g(Xk))