

P= 56 #atm
T= 450 #K
R= 0.08206 #atm*l/mol*K
Tc= 405.5 #K
Pc= 111.3 #atm
a= 27*(R*Tc)**2/(64*Pc)
b= R*Tc/(8*Pc)



def f_van (v_molar):
	return (P+a/v_molar**2)*(v_molar-b)-R*T


#funcion NR
def Newton_Rhapson (f,xk,h):

	#derivada por diferencias finitas centrales
	def dif_central (yi_menos1, yi_mas1, h):
		return (yi_mas1-yi_menos1)/(2*h)

	k=0
	Es=1e-4 # %
	Ea=100 #%

	while Ea>Es and k<1000:
		fprima=dif_central(f(xk-h),f(xk+h),h)
		xk_mas1=xk-(f(xk)/fprima)
		Ea=100*abs((xk_mas1-xk)/xk_mas1)
		xk=xk_mas1
		k=k+1

	if Ea<Es:
		return {"raiz":xk_mas1,"iteraciones":k, "f(x)":f(xk_mas1)}

	else:
		print ("no converge, pruebe otra xk")


solucion=Newton_Rhapson(f_van,2,0.1)
print (solucion)

