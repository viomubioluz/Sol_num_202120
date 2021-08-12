# Regla falsa

from math import exp

def f (x):
	return exp(-(x+1))-1


def regla_falsa(x_l, x_u, funcion, Es=1e-4):
	y_u=funcion(x_u)
	y_l=funcion (x_l)
	k=0
	Ea=100 #porcentaje
	Xr=x_u-(y_u*(x_l-x_u))/(y_l-y_u)

	while Ea>Es and k<1000:
		y_r=funcion(Xr)
		if y_r*y_l<0:
			x_u=Xr
			y_u=y_r
		else:
			x_l=Xr
			y_l=y_r

		Xr_ant=Xr
		Xr=x_u-(y_u*(x_l-x_u))/(y_l-y_u)
		Ea=100*abs((Xr-Xr_ant)/Xr)
		k+=1
	return {"solucion":Xr, "f(xr)":y_r, "iteraciones": k}



resultado=regla_falsa(-2, 0, f)
print (resultado["iteraciones"])



