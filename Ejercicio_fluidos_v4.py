from math import pi, log10
from metodos_abiertos import newton_rhapson as nr
from matplotlib.pyplot import plot, show, xlabel, ylabel, title, xticks


D=27/1000           # m
L=1.2               # m
e=0.0015/1000       # m
g=9.81              # m*s-2
rho=998             # kg*m-3
mu=1.002/1000       # kg*m-1*s-1

gamma=rho*g         # N*m-3 
A=pi*D**2/4       # m2  Area del circulo
nu=mu/rho           # m2*s-1  

# Datos brutos
presion1=[46,38,32,28,22,18,14,12,10,8,6,6]  # mbar
presion2=[.8,.8,.85,.85,.9,.9,.9,.95,.95,.95,.95,1] # bar

n= len(presion1)  # Cantidad de datos

#definiendo la funcion para el balance de energia
def balance_energia (Q):         # Q en m3/s
	pb=(-0.30*(Q*1000)+1.0)*1e5  # Pa, se convierte Q a L/s y pb de bar a Pa  
	V=Q/A 						 # velocidad en m/s
	Re=V*D/nu                    # adimensional
	if Re<2000:
		f=64/Re                  # adimensional
	else:
		f=1/(-1.8*log10(6.9/Re+((e/D)/3.7)**1.11))**2    # adimensional
	
	hL=f*(L/D)*(V**2/(2*g))  # m
	
	return (p1-p2+pb)/gamma-hL

# solucion por Newton Rhapson
flujos=[] # L/min
k=0 # contador para acceder a los elementos de la lista (posiciones)
while k<n:
	p1=presion1[k]*100 # coversion de mbar a bar y de bar a Pa
	p2=presion2[k]*1e5 # conversion de bar a Pa
	solucion=nr(balance_energia,0.01,1e-4)
	flujos.append(solucion["raiz"]*6e4) # conversion de Q m3/s a L/min 
	k+=1

#print (len(presion1))

# Generando grafica de resultados
tiempo=range (0,60,5) # min , lista de tiempos
plot(tiempo,flujos,"-ok")
xlabel ("t [min]")
xticks(tiempo)
ylabel ("flujo volumetrico [L/min]")
title ("Flujo volumetrico vs Tiempo")
show()