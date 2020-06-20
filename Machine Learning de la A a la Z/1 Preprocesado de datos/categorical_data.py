import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values # dataset[['Country','Age','Salary']].values
y = dataset.iloc[:, 3].values # dataset['Purchased'].values

# TRATAMIENTO DE LOS NaN
from sklearn.impute import SimpleImputer
# Transformador de imputación para completar valores perdidos.  
"""
class sklearn.impute.SimpleImputer(missing_values=nan, strategy='mean', fill_value=None, verbose=0, copy=True, add_indicator=False)
# missing_values : Definicion de valores faltantes (number, string, np.nan (predeterminado) o None). Los que coinciden con missing_values serán transformados.
# strategystring : La estrategia que se reemplazara / media : 'mean'
"""

imputer = SimpleImputer(strategy="mean")  # Los valores 'NaN' seran reemplazado por ('la media') Toma como conjunto de valores todos los de la columna

# medias en columnas 1,2 / el ultimo valor no esta considerado por eso se pone hasta el 3 
imputer = imputer.fit(X[:, 1:3])  # fit('Que datos le aplicare el imputer')

# Cambiar valores por dichas medias
X[:, 1:3] = imputer.transform(X[:, 1:3]) # transform() : devuelve y asigna los valores desconocidos




"""
Categorias para usuarios osea un usario vive en "Francia" y no puedo sumar "franacia"
"""
# Codificar datos categóricos, con un libreria OBIo.
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X = LabelEncoder()
#  fit_transform('Las columnas categoricas que quiera modificar') lo transforma a numeros                    
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()


ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],    # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
    remainder='passthrough'                         # Leave the rest of the columns untouched
)
X = np.array(ct.fit_transform(X), dtype=np.float)

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# PS: IMPORTANTE. En la siguiente clase de Python, la sintaxis de 'NaN' ha sido 
# reemplazado por 'np.nan' en la última actualización de la librería sklearn.
