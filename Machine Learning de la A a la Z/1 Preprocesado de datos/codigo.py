import numpy as np
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values # dataset[['Country','Age','Salary']].values
y = dataset.iloc[:, 3].values # dataset['Purchased'].values

# TRATAMIENTO DE LOS NaN
from sklearn.impute import SimpleImputer 

# Los valores 'NaN' seran reemplazado por ('la media') Toma como conjunto de valores todos los de la columna
imputer = SimpleImputer(strategy="mean")  

# medias en columnas 1,2 
imputer = imputer.fit(X[:, 1:3])  # fit('Que datos le aplicare el imputer')

# Cambiar valores por dichas medias
X[:, 1:3] = imputer.transform(X[:, 1:3]) # transform() : devuelve y asigna los valores desconocidos


""" "Francia" no me sirve, no se compara con numeros
"""
# Codificar datos categóricos, con un libreria OBIo.
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X = LabelEncoder()
#  fit_transform('Las columnas categoricas que quiera modificar') lo transforma a numeros                    
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

# Trasforma a DUMMYS
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()


ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],    
    remainder='passthrough')

X = np.array(ct.fit_transform(X), dtype=np.float)

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
# X_train : X de entrenamiento | X_test : x de test
# y_train : y de entrenamiento | y_test : y de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# X : independientes ||  y :dependientes(a predecir)
# test_size : %tamaño del test
# random_state: semilla


# Escalado de variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
# Usamos el mismo tipo de escalado "sc_X" en ambos "X_train" y "X_test"
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

