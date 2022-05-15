import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

## Ejercicios
#
#1. Obtén una matriz de 2×2 multiplicando dos matrices de 4×2 y 2×4
#2. Dibuja un vector y aplícale una transformación matricial de rotación. Dibuja el vector resultante.
#3. Dibuja un vector y aplícale una transformación matricial de escalado. Dibuja el vector resultante.
#4. Busca en internet cómo tomar la n potencia de una matriz, y compútala.
#5. Busca en internet cómo encontrar los vectores y valores propios de una matriz y compútalos.

# 1.

cuatroDos = np.random.rand(4,2)
dosCuatro = np.random.rand(2,4)
DosDos = np.dot(dosCuatro, cuatroDos)

# 2.

def graph() : 
    fig, axes = plt.subplots()
    axes.set_xlim([-5,5])
    axes.set_ylim([-5,5])
    return fig, axes

# make graphic object
fig, axes = graph()

# define vector
v = np.array([2,3])
# draw arrow ==> Axes.arrow(x, y, dx, dy, **kwargs). ==> Add an arrow to the Axes. ==> This draws an arrow from (x, y) to (x+dx, y+dy).
axes.arrow(0, 0, v[0], v[1], shape='full', width=0.01, head_width=0.4, color='red')

# define rotation matrix
def anticlockwiseRotMatrix(phi) :  
    return np.matrix([[math.cos(phi), -math.sin(phi)], [math.sin(phi), math.cos(phi)]])

# rotate vector
v_rot = np.dot(anticlockwiseRotMatrix(90), np.transpose(v))

v_rot = np.asarray(v_rot)
v_rot = v_rot.reshape(-1)

axes.arrow(0, 0, v_rot[0], v_rot[1], shape='full', width=0.01, head_width=0.4, color='blue')
plt.show()

# 3.

def scaleMatrix(factor) : 
    return np.matrix([[factor, 0], [0, factor]])

v_scaled = np.dot(scaleMatrix(0.5), v)

v_scaled = np.asarray(v_scaled)
v_scaled = v_scaled.reshape(-1)

fig, axes = graph()

axes.arrow(0, 0, v_scaled[0], v_scaled[1], shape='full', width=0.01, head_width=0.4, color='green')
axes.arrow(0, 0, v[0], v[1], shape='full', width=0.01, head_width=0.4, color='red')
plt.show()

# 4.

M = np.matrix([[1, 2], [3, 4]])
n = 3
print("numpy : \n" , np.linalg.matrix_power(M, n))

def m_power(M, n):
    res = M
    for i in range(1,n):
        res = np.dot(res, M)
    return res

print("iterative : \n", m_power(M, n))

# 5.

eigenvalues, featurevectors = np.linalg.eig(M)

print("Autovalor(es):\n", eigenvalues)
print("Vector(es) de características:\n", featurevectors)
