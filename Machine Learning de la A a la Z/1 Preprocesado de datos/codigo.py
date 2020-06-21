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
