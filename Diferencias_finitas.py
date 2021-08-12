#diferencias finitas hacia adelante
def dif_adelante (fxi_mas1, fxi, h):
	return (fxi_mas1-fxi)/h

#diferencia hacia atras
def dif_atras (fxi, fxi_menos1, h):
	return (fxi-fxi_menos1)/h 

#diferencia central
def dif_central (fxi_mas1, fxi_menos1, h):
	return (fxi_mas1-fxi_menos1)/(2*h)

#Erro relativo verdadero, en porcentaje
def error (valor_true, valor_aprox):
	return 100*abs((valor_true-valor_aprox)/(valor_true))

#calculando la pendiente con un h=0,2
fprima_adelante=dif_adelante (0.05596, 0.1310, 0.2)
fprima_atras=dif_atras (0.1310, 0.4221, 0.2)
fprima_central=dif_central (0.05596, 0.4221, 0.2)

print ("la pendiente calculada es   ")
print ("diferencia hacia adelante: ", fprima_adelante, "y su error es:", error (-0.6370, fprima_adelante))
print ("diferencia hacia atras: ", fprima_atras, "y su error es:", error (-0.6370, fprima_atras))
print ("diferencia central: ", fprima_central, "y su error es:", error (-0.6370, fprima_central))

#calculando la pendiente con un h=0,1
fprima_adelante_=dif_adelante (0.08328, 0.1310, 0.1)
fprima_atras_=dif_atras (0.1310, 0.2222, 0.1)
fprima_central_=dif_central (0.08328, 0.2222, 0.1)

print ("------------")
print ("diferencia hacia adelante: ", fprima_adelante_, "y su error es:", error (-0.6370, fprima_adelante_))
print ("diferencia hacia atras: ", fprima_atras_, "y su error es:", error (-0.6370, fprima_atras_))
print ("diferencia central: ", fprima_central_, "y su error es:", error (-0.6370, fprima_central_))