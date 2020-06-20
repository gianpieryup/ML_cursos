### Antes

Te recomiendo llevar un curso de python completo, en udemy o en youtube (a tu gusto)

# Pre-procesado de datos

Un conjunto de datos (conocido también por el anglicismo `dataset`, comúnmente utilizado en algunos países hispanohablantes) es una colección de datos habitualmente tabulada.

````python
# Estas librerias ya vienen por defecto en python.
import numpy as np		# Matrices, Algebra ,etc
import matplotlib.pyplot as plt  # Graficas, visual

# pandas : Carga, Manipulacion de datos(para leer el .csv,...)
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Data.csv')

# Quiero separar las variables dependientes de las independientes 
# iloc["filas","columnas"]
# [:] todas 	||    [:-1]  todas  menos la ultima
X = dataset.iloc[:, :-1].values     # .values (Solo los valores, sin las posiciones)

# todas las filas / pero solo la columna 3
y = dataset.iloc[:, 3].values
````



#### Datos Faltantes o Desconocidos

> IMPORTANTE: **Cambios en Python 3.7**, la sintaxis de 'NaN' ha sido reemplazado por 'np.nan' en la última actualización de la librería sklearn.

````python
# Con que reemplazar los NaN: CRITERIO => Por la media de los datos

# (import Imputer : esta clase fue descontinuada) 
from sklearn.impute import SimpleImputer

"""
class sklearn.impute.SimpleImputer(missing_values=nan, strategy='mean', fill_value=None, verbose=0, copy=True, add_indicator=False)
- missing_values : Definicion de valores faltantes (number, string, np.nan (predeterminado) o None).Los que coinciden con missing_values serán transformados.
- strategystring : La estrategia que se reemplazara 'mean' (predeterminada)
"""

# Los valores 'NaN' seran reemplazado por ('la media') Toma como conjunto de valores todos los de la columna
imputer = SimpleImputer(strategy="mean")  

# medias en columnas 1,2 / el ultimo valor no esta considerado por eso se pone hasta el 3 
imputer = imputer.fit(X[:, 1:3])  # fit('Que datos le aplicare el imputer')

# Cambiar valores por dichas medias
X[:, 1:3] = imputer.transform(X[:, 1:3]) # transform() : devuelve y asigna los valores desconocidos
````

#### Datos Categóricos

Una columna que en ves de tener datos numéricos tiene de otro tipo como string "Francia",etc. Las transformaremos en datos numéricos 

````python
# Codificar datos categóricos, con un libreria OBIo.
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer


# LabelEncoder le da igual que tipo de dato lo trasnforma a numero
# ["Pedro","Juan","Roberto","Juan"] = > [2,1,0,1]
labelencoder_X = LabelEncoder()
#  fit_transform('Las columnas categoricas que quiera modificar')                 
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])


# Para crear las variables dummys(codificacion de un solo 1 por linea)
"""
Variables dummys o onehotencoder
0 => (1,0,0)
2 => (0,0,1)
1 => (0,1,0)
"""
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],    # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
    remainder='passthrough'                         # Leave the rest of the columns untouched
)
X = np.array(ct.fit_transform(X), dtype=np.float)

# Cuando es una variable binaria como SI o NO solo nesecito numeros [1,2]
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
````

### Como dividir el data set en entrenamiento y test

````python
# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
"""
X_train : variables independientes que se usaran para entrenar el algortimo
X_test : variables para testear que el algoritmo funciona correctamente 
y_train : valores de prediccion para que aprenda a predecir
y_test : variables para evaluar la eficacia 

test_size: tamaño en porcentaje para usar en testing
random_state : ponle 0
"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
````

> TIP : Nuestro algoritmo intentara predecir con la menor cantidad de error posible los resultados, pero existe un problema llamado **overhiting** que es cuando el algoritmo se aprende de memoria los resultados, entonces erra mucho si le doy un nuevo dato

### Escalado de variables

Cuando tengo mi tabla de valores, agarro un par de puntos (x,y) y (z,w) , calculo la distancia entre ellos puede ocurrir que la diferencia  `x - y <<< z - w` .Por lo cual se perdería la información. Para solucionar esto se cambia los valores de `-1 a 1` donde `-1` es el menor valor y `1` es el máximo. 

Existen dos formas de hacer esto la `estandardisacion` o la `normalizacion`

- estandarización : x-media/desviación estándar
- normalización : x-min/Max-min `ver que varia de [0,1]`

````python
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)#de lo anterior
X_test = sc_X.transform(X_test)
````

