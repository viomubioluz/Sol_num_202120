# ndarray
import numpy as np 
from numpy.linalg import det

x=[1,2,3,4]
y=[5,6,7,8]


v=np.array(x)
u=np.array(y)
#print (u, y)

# operaciones vectores
#print (v**2, v)
#print ((u+v)*3)

# producto punto 
c=v@u 
#print (c)
#print (type(v))

#print (v.shape, v)

#print (np.arange(0,10,2)) # solo genera enteros y el rango final no es inclusivo
#print (np.linspace(0,15.5,5)) # inicial, final (inclusivo) y genera float
#print (np.ones(5))
#print (np.zeros(5))

# aplicacion de funciones nativas de python en vectores
#print (min(u))
#print (max(u))
#print (sum(u))

#print (u.mean())
#print (u.argmax())
#print (u.cumsum())

# como acceder a los elementos de un vector
L=v[0]
tt=v[1:4]
#print (tt)
t=v[:3]
#print (t)

#print (v.size)

#calculando la norma
vector=np.array([123,432,456,765])



# forma manual
c1=vector [0]**2
c2=vector [1]**2
c3=vector [2]**2
c4=vector [3]**2
prod=c1+c2+c3+c4
#print ((prod)**0.5)


print ("--------------- matrices-------------")

vector1=np.array([22,33,44,55])
vector2=np.array([21,32,43,51])
vector3=np.array([77,88,99,66])

lista=[vector1,vector2,vector3,vector3]
matriz=np.array(lista)
#print (matriz, "......", matriz.shape, vector1.shape)


matrizfila=np.array([vector1])
#print (matrizfila, matrizfila.shape)

matrizcolumna=matrizfila.T 
#print (matrizcolumna, matrizcolumna.shape)
#print ("...")
#print (matrizcolumna.flatten())

# multiplicacion de matrices
producto=matriz@matrizcolumna
#print (producto)

# escribiendo una matriz
R=[[1,2,3],[3,4,3],[5,6,3]]
M=np.array(R)
#print (M) 
#print (det(M))

# generadores de matrices
#print (np.zeros((2,2)))
#print (np.identity(3))

# accediento a los elemento de una matriz
#print (M[:,1])
#print (M[2,:])

# extrayendo una submatriz
#print (M[0:2,0:2])

bb=np.zeros((5,5))
#print (bb)
cc=M[0:2,0:2]
bb[1:3,1:3]=cc
print (bb)

