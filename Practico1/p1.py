{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Semana 1\n",
    "\n",
    "## Introducción\n",
    "\n",
    "El objetivo de este práctico es obtener mínimos conocimientos sobre la sintaxis de Python, en especial el manejo de matrices, vectores y sus operaciones.\n",
    "\n",
    "Durante el práctico y en el curso en general vamos a utilizar tres librerías fundamentales.\n",
    "1. *numpy*: se usa para hacer operaciones con vectores y matrices. Es más eficiente que los arreglos por defecto de Python.\n",
    "2. *pandas*: se usa para manejo de datos e importación de base de datos.\n",
    "3. *pyplot*: se usa para graficar\n",
    "\n",
    "Procedemos a importarlas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "lzUxupC1OLGn"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "KJCTxMLxOLGp"
   },
   "source": [
    "## Funciones\n",
    "\n",
    "Las funciones de Python son objetos que aceptan como argumentos otros objetos. La sintaxis es de la forma funcion(x,y,z,...) donde funcion indica el nombre de la función, y los paréntesis delimitan los argumentos, separados por comas. Distintas funciones van a requerir distintos argumentos. Hay funciones que no requieren argumentos, hay funciones que requieren un número fijo de argumentos, y funciones que pueden aceptar argumentos opcionales.\n",
    "\n",
    "Python y sus paquetes básicos vienen con un montón de funciones. Para obtener ayuda sobre una función y sus argumentos, podés escribir ?funcion en la consola para invocar la ayuda.\n",
    "\n",
    "Más adelante veremos como crear funciones propias.\n",
    "\n",
    "## Vectores\n",
    "\n",
    "Los vectores en Python pueden ser objetos de distintos tipos:\n",
    "- numéricos (como se imaginarán, números)\n",
    "- caracteres (caracteres alfanumericos)\n",
    "- otros\n",
    "\n",
    "Si queremos crear vectores, lo hacemos usando la función *array* de la librería numpy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "39NegPP_OLGr"
   },
   "outputs": [],
   "source": [
    "v_numerico = np.array([1,2,3,4])\n",
    "v_caracter = np.array([\"a\",\"b\",\"c\",\"d\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "-h8osYhEOLGs"
   },
   "source": [
    "Para visualizar el contenido, escribimos el nombre de la variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "5bB3bKBnOLGs",
    "outputId": "43dbf0fb-044f-4878-88a1-bf763eb38317"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v_numerico"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "zVpdArgwOLGt"
   },
   "source": [
    "Si no queremos listar todos los elementos, podemos generar automáticamente una lista con las siguientes funciones:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "b1hOANBxOLGt",
    "outputId": "5e45fef4-8577-4895-b274-c430e4054c47"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.1 0.3 0.5 0.7 0.9 1.1]\n",
      "[0.1 0.3 0.5 0.7 0.9]\n",
      "[0.1 0.3 0.5 0.7 0.9 1.1]\n"
     ]
    }
   ],
   "source": [
    "v1 = np.linspace(0.1, 1.1, 6)\n",
    "v2 = np.arange(0.1, 1.1, 0.2)\n",
    "v3 = np.arange(0.1, 1.11, 0.2)\n",
    "print(v1)\n",
    "print(v2)\n",
    "print(v3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "QrMETimHOLGu"
   },
   "source": [
    "Es importante observar las diferencias entre las funciones: con *linspace* dividimos el intervalo $ [0.1, 1.1] $ en 6 partes iguales. Por otro lado, en *arange* indicamos el valor más chico de la lista, un valor límite y un valor para saltos.\n",
    "\n",
    "En principio es bastante útil conceptualizar los vectores en Python tal cual lo haríamos en álgebra lineal. Es posible acceder a entradas particulares de los vectores usando el operador $[·]$:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "Ykp7GfqFOLGv",
    "outputId": "87775553-7b9a-44ef-c0c2-97e87039c9b7"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.5\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1.1"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(v1[2])\n",
    "v1[-1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "2u0qE-gNOLGv"
   },
   "source": [
    "El índice -1 hace referencia al último elemento de la lista.\n",
    "\n",
    "Además, podemos obtener subsecciones de las entradas de los vectores usando también el operador *:* :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "YvYlp701OLGv",
    "outputId": "61eca7de-d60d-4b22-9bb2-8bab977c1385"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.7, 0.9])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "v1[3:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "sxF24H7POLGw"
   },
   "source": [
    "Muchas funciones son aplicables a vectores, es decir, funciones vectorizadas. Veremos algunas de las más comunes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "ChDhCooMOLGw",
    "outputId": "7ba9ed71-34e8-4445-9a5f-0e5b2c05de79"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.6\n",
      "2.8600000000000008\n",
      "[0.2 0.6 1.  1.4 1.8 2.2]\n",
      "[0.01 0.09 0.25 0.49 0.81 1.21]\n"
     ]
    }
   ],
   "source": [
    "print(sum(v1))\n",
    "print(np.dot(v1, v3))\n",
    "print(v1 + v3)\n",
    "print(v1*v3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "jPYjbVUPOLGx"
   },
   "source": [
    "El comando *sum* devuelve la suma de todos los elementos de la lista, el comando *dot* de NumPy devuelve el producto interno entre ambos vectores y la suma y producto de vectores se hace coordenada a coordenada.\n",
    "\n",
    "También hay funciones útiles para la estadística:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "IecALw2QOLGx",
    "outputId": "7210ac81-2232-45b1-a93a-0bba154643b1"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.6\n",
      "0.34156502553198664\n"
     ]
    }
   ],
   "source": [
    "print(np.mean(v1))\n",
    "print(np.std(v1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "_p_3z6bXOLGy"
   },
   "source": [
    "El comando *mean* devuelve la media muestral del vector, mientras que *std* calcula la desviación estándar de la muestra."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ZfjH_aylOLGz"
   },
   "source": [
    "## Ejercicios\n",
    "\n",
    "1. Explora las opciones de las funciones *seq() , rep()* y *length()*\n",
    "1. Calcula la media de un vector sin usar la función *mean()*\n",
    "\n",
    "## Matrices\n",
    "\n",
    "Ahora pasamos al uso de matrices en Python. En principio, una matriz la podemos definir a partir de un vector, de hecho es un vector de vectores. Para crearlas utilizamos el comando *matrix()* de Num"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "FVt7nE3DOLG0",
    "outputId": "c645abf3-56ae-4e42-8e92-7414c648e54d"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [3 4]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "matrix([[1, 2],\n",
       "        [3, 4]])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A = np.matrix('1 2; 3 4')\n",
    "B = np.matrix([[1, 2], [3, 4]])\n",
    "\n",
    "print(B)\n",
    "A"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0KcMm8hZOLG1"
   },
   "source": [
    "Observar las dos formas de definir la misma matriz. También podemos acceder a los elementos de la matriz como con los vectores. \n",
    "\n",
    "Es importante recordar que los arrays en Python empiezan en 0, por lo que los índices de las matrices $2 \\times 2$ varían entre 0 y 1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "AHM-sbmiOLG1",
    "outputId": "0352d0da-6f14-4ad1-f408-3f2e44c863f0"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "B[0,1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "1VShL616OLG2"
   },
   "source": [
    "## Ejericicio\n",
    "Entender qué está pasando en el siguiente código:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "id": "U5zg7FE-OLG2",
    "outputId": "92952ecc-977f-4b9e-9d26-0b6cd35018cd"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]]\n",
      "[[2]\n",
      " [4]]\n"
     ]
    }
   ],
   "source": [
    "print(B[0,:])\n",
    "print(B[:,1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "XTX1q5GgOLG3"
   },
   "source": [
    "También podemos crear matrices aleatorias usando el comando *rand*:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "id": "ucSXKbg7OLG3",
    "outputId": "71b8cb9f-e24e-4cd0-f255-c656df88ca18"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.60503393, 0.90288674, 0.04888504],\n",
       "       [0.88337407, 0.48961026, 0.96569456]])"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "C = np.random.rand(2,3)\n",
    "C"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "nP5PtsMGOLG4"
   },
   "source": [
    "## Gráficas y operaciones con matrices\n",
    "\n",
    "Al igual que en el caso de los vectores, podemos sumar dos matrices y también multiplicarlas coordenada a coordenada. Para multiplicar usamos el comando *dot*:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "id": "jtIzyXNsOLG4",
    "outputId": "71a36f4b-3312-4e30-f2cb-57da9ec2597d"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "matrix([[2.37178207, 1.88210726, 1.98027417],\n",
       "        [5.34859807, 4.66710126, 4.00943338]])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.dot(A,C)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "qdQ6SDyYOLG4"
   },
   "source": [
    "Vamos a trabajar con vectores de $\\mathbb{R}^2$, de paso vamos a ver cómo podemos graficarlos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "id": "aiiaQvizOLG5"
   },
   "outputs": [],
   "source": [
    "v = np.matrix('1 ; 1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "id": "XzHtzEUyOLG5",
    "outputId": "1922f771-15b9-4ac9-fcbb-b5c82ff61d8c"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots()  # Create a figure containing a single axes.\n",
    "\n",
    "ax.set_xlim([-6, 6])\n",
    "ax.set_ylim([-6, 6])\n",
    "\n",
    "ax.arrow(0, 0, v[0,0], v[1,0], shape='full', width=0.01, head_width=0.2)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "4R1lfqlWOLG6"
   },
   "source": [
    "Ahora agregamos el producto de la matriz A con el vector v."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "id": "20DeRn3dOLG6",
    "outputId": "7ae343fb-6ba9-465c-d265-47ded1bee974"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "v2 = np.dot(A, v)\n",
    "fig2, ax2 = plt.subplots()  # Create a figure containing a single axes.\n",
    "\n",
    "\n",
    "ax2.set_xlim([-10, 10])\n",
    "ax2.set_ylim([-10, 10])\n",
    "\n",
    "ax2.arrow(0, 0, v[0,0], v[1,0], shape='full', width=0.01, head_width=0.4)\n",
    "ax2.arrow(0, 0, v2[0,0], v2[1,0], shape='full', width=0.01, head_width=0.4, color='red')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "aRYnqnKJOLG7"
   },
   "source": [
    "## Ejercicios\n",
    "\n",
    "1. Obtén una matriz de 2×2 multiplicando dos matrices de 4×2 y 2×4\n",
    "1. Dibuja un vector y aplícale una transformación matricial de rotación. Dibuja el vector resultante.\n",
    "1. Dibuja un vector y aplícale una transformación matricial de escalado. Dibuja el vector resultante.\n",
    "1. Busca en internet cómo tomar la n potencia de una matriz, y compútala.\n",
    "1. Busca en internet cómo encontrar los vectores y valores propios de una matriz y compútalos.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "SaT4Imr3OLG7"
   },
   "source": [
    "## Dataframes\n",
    "\n",
    "Los data frames son la clase de objeto más conveniente para almacenar datos de todo tipo. Los vectores y matrices están restringidos a almacenar un solo tipo de dato, sea numérico, caracter o lógico. Los data frames, en cambio, pueden almacenar varios de estos datos.\n",
    "\n",
    "La forma más simple de inicializar un data frame es a partir de una matriz. Aunque, cotidianamente, leeríamos los datos desde un archivo de texto. La librería encargada de realizar este tipo de datos se llama *pandas*."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "id": "-yy2FM2JOLG7",
    "outputId": "0d0d0867-e284-42c2-f753-ed3fdcad75bb"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.78084565, 0.98528035, 0.43712711],\n",
       "       [0.50195108, 0.43392577, 0.13968129],\n",
       "       [0.3039054 , 0.2468346 , 0.21727261]])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "M = np.random.rand(3,3)\n",
    "M"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "id": "mR1nOlW5OLG7",
    "outputId": "db55c463-4e3e-4166-f4ee-03435a17cc85"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.780846</td>\n",
       "      <td>0.985280</td>\n",
       "      <td>0.437127</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.501951</td>\n",
       "      <td>0.433926</td>\n",
       "      <td>0.139681</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.303905</td>\n",
       "      <td>0.246835</td>\n",
       "      <td>0.217273</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          0         1         2\n",
       "0  0.780846  0.985280  0.437127\n",
       "1  0.501951  0.433926  0.139681\n",
       "2  0.303905  0.246835  0.217273"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = pd.DataFrame(M)\n",
    "d"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "HRlaoXfOOLG7"
   },
   "source": [
    "Los dataframes necesariamente tienen que tener nombres de columnas. Como no los proveímos al inicializarla, fueron generados automáticamente. A continuación, agregaremos una nueva columna que contenga un vector de caracteres."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "id": "i4AeBJrtOLG8",
    "outputId": "13f339cc-d14e-43f5-ffc8-0ae43de0791e"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>char</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.780846</td>\n",
       "      <td>0.985280</td>\n",
       "      <td>0.437127</td>\n",
       "      <td>a</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.501951</td>\n",
       "      <td>0.433926</td>\n",
       "      <td>0.139681</td>\n",
       "      <td>b</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.303905</td>\n",
       "      <td>0.246835</td>\n",
       "      <td>0.217273</td>\n",
       "      <td>c</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          0         1         2 char\n",
       "0  0.780846  0.985280  0.437127    a\n",
       "1  0.501951  0.433926  0.139681    b\n",
       "2  0.303905  0.246835  0.217273    c"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d[\"char\"] = np.array([\"a\",\"b\",\"c\"])\n",
    "d"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "BeUWCzBOOLG8"
   },
   "source": [
    "Podemos realizar operaciones sobre las columnas de d, a modo de ejemplo:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "id": "HmvZ2fCwOLG8",
    "outputId": "bea15d2e-1ae9-4253-c0a1-3a6af7fad484"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    2.203253\n",
       "1    1.075558\n",
       "2    0.768013\n",
       "dtype: float64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.sum(axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "RCEQGfegOLG8"
   },
   "source": [
    "Observar que nos devuelve la suma de los elementos de cada columna.\n",
    "\n",
    "## Ejercicios\n",
    "\n",
    "1. Calcula la suma de todas las filas como en el ejemplo anterior.\n",
    "1. Crea un dataframe de $4 \\times 10$ y calcula su media y desviación estándar para cada columna.\n",
    "1. Crea un dataframe con datos mixtos (columnas de distintos tipos). Luego separa el dataframe en dataframes de columnas del mismo tipo.\n",
    "1. Investigar cómo puedo obtener una columna de un DataFrame.\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "name": "semana1_MIF.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
