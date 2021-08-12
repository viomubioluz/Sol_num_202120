#Diferencias finitas hacia adelante
def dif_adelante (yi_mas1, yi, h):
	return (yi_mas1-yi)/h 

#Diferentecias finitas hacia atras
def dif_atras (yi, yi_menos1, h):
	return (yi-yi_menos1)/h

#Diferencias centrada
def dif_central (yi_mas1, yi_menos1, h):
	return (yi_mas1-yi_menos1)/(2*h)

#Error relativo verdadero
def error (valor_true, valor_aprox):
	return 100*abs((valor_true-valor_aprox)/valor_true)

#Calculando la pendiente para un h=0,2
fprima_adelante= dif_adelante(0.05596, 0.1310, 0.2)
fprima_atras= dif_atras(0.1310, 0.4221, 0.2)
fprima_central= dif_central(0.05596, 0.4221, 0.2)

# Calculando la pendiente de la funcion
fprima= -0.6370
print("A. La pendiente calculada por:")
print (f"	-Diferencia hacia adelante es {fprima_adelante:.3f} y su error {error(fprima, fprima_adelante):.1f}%")
print (f"	-Diferencia hacia atras es {fprima_atras:.3f} y su error {error(fprima, fprima_atras):.1f}%")
print (f"	-Diferencia central {fprima_central:.3f} y su error {error(fprima, fprima_central):.1f}%")

#Calculando la pendiente para un h=0,1
fprima_adelante= dif_adelante(0.08322, 0.1310, 0.1)
fprima_atras= dif_atras(0.1310, 0.2222, 0.1)
fprima_central= dif_central(0.08322, 0.2222, 0.1)

#Calculando la pendiente de la funcion
print ("                              ")
print("B. La pendiente calculada por:")
print (f"	-Diferencia hacia adelante es {fprima_adelante:.3f} y su error {error(fprima, fprima_adelante):.1f}%")
print (f"	-Diferencia hacia atras es {fprima_atras:.3f} y su error {error(fprima, fprima_atras):.1f}%")
print (f"	-Diferencia central {fprima_central:.3f} y su error {error(fprima, fprima_central):.1f}%")