from math import exp

# Regla Falsa 
def regulaFalsi(x_l, x_u, funcion, Es= 1e-6):
	y_l=funcion(x_l)
	y_u=funcion(x_u)
	k=0
	Ea=100
	Xr=(x_u-x_l)/2
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

	return {'solucion': Xr, 'f(x)': y_r, 'iteraciones': k} 


#funcion
def funcion (x):
	return exp(-(x+1))-1

#Tanteo de limites iniciales para empezar a encontrar la raíz
a= 5
b= -5
#ya= funcion(a)
#yb= funcion(b)
#print(ya, yb, ya*yb)

resultado= regulaFalsi(a, b, funcion)
print (resultado)

