# Regla Falsa
from math import exp 
# funcion
def funcion (x):
	return (667.38/x)*(1-exp(-0.146843*x))-40

x_l=12
x_u=16
y_l=funcion(x_l)
y_u=funcion(x_u)
k=0
Es=1e-6
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

Xsol=Xr
print ("la raiz esta en: ", Xsol )
print ("k= ", k)
