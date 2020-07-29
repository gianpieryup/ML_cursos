import numpy as np
import numpy.linalg as npl

x = np.array([0,2,2.5,1,4,7])
y = np.array([5,10,9,0,3,27])
z = np.array([0,1,2,3,6,2])

A = np.ones((6,3))
A[:,1] = x
A[:,2] = z

A_ = np.dot(A.T,A)
b = np.dot(A.T,y)
c = np.dot(npl.inv(A_),b)

print("La ecuacion es: \n y =",c[0],"+",c[1],"*x +",c[2],"*z")