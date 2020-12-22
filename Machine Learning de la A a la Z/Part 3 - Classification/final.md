## Conclusión de la Parte 3 - Clasificación

En esta Parte 7, has aprendido acerca de 7 modelos de clasificación. Del mismo modo que vimos en la Parte 2 - Regresión, puede que tengas algunas preguntas interesantes ahora que conoces este mundo:

1. ¿Cuales son los pros y los contras de cada modelo?
2. ¿Cómo sé qué modelo debo elegir para resolver mi problema?
3. ¿Cómo puedo mejorar cada uno de estos modelos ?

Resolvamos cada pregunta una por una:

**1. ¿Cuales son los pros y los contras de cada modelo?**

En esta clase encontrarás una chuleta que te dará todos los pros y contras de cada modelo de clasificación.

**2. ¿Cómo sé qué modelo debo elegir para resolver mi problema?**

Al igual que con los modelos de regresión, primero tendrás que averiguar si tu problema es o no es lineal. En la Parte 10 - Selección de Modelos hablaremos precisamente de este y otros temas. Una vez lo sepas,

- Si tu problema es lineal, deberás intentar crear un modelo de Regresión Logística o bien SVM.

- Si tu problema no es lineal, entonces tenemos varias técnicas donde elegir, como K-NN, Naïve Bayes, Árboles de Decisión o Random Forest.

Desde un punto de vista empresarial, entonces deberías usar:

- Regresión Logística o Naïve Bayes cuando quieras ordenar tus predicciones por probabilidad. Por ejemplo, deberías usar estas técnicas si quieres crear un ranking de clientes desde el más probable al menos probable que compre un producto. Esto permite crear objetivos específicos para las campañas de marketing, por ejemplo. Y por supuesto, si tu problema de empresa es lineal, mejor utiliza la regresión logística, y si no lo es, intenta con Naïve Bayes.
- SVM cuando quieras predecir a qué segmento pertenece un cliente. Los segmentos pueden ser cualquier conjunto de características que definan a los clientes, como los que identificaremos en la Parte 4 - Clustering.
- Los árboles de decisión cuando necesites tener una interpretación clara de los resultados modelizados.
- Y por último, Random Forest cuando busques un mejor resultado de predicción y te preocupe menos la interpretación de los modelos.

**3. ¿Cómo puedo mejorar cada uno de estos modelos ?**

Igual que en la parte 2, en la Parte 10 - Selección de Modelos, la segunda sección está dedicada a los Ajustes de Parámetros que permite mejorar la eficacia de nuestros modelos ajustando los valores de los parámetros. Como habrás comprobado, existen dos tipos de parámetros en nuestros modelos:

- los parámetros que el modelo aprende, como los coeficientes de la Regresión Lineal,
- los hiper parámetros del algoritmo.

En este último caso, los hiper parámetros son parámetros que el algoritmo no aprende, si no que son fijos y forman parte de las ecuaciones de los modelos. Por ejemplo, el parámetro lambda de regularización o el factor de penalización C son hiper parámetros. Hasta el momento hemos tomado los valores por defecto y no nos hemos preocupados de afinar su valor óptimo para mejorar la eficacia del modelo. Entontrar el valor óptimo es parte del Ajuste de Parámetros, así que si estás interesado en descubrir cómo hacerlo, te recomiendo ir directamente a la Parte 10 del curso donde veremos juntos cómo hacerlo.

Y como BONUS adicional, encontrarás también algunos apuntes adicionales acerca de la Regularización.

Entonces enhorabuena, porque has completado la Parte 3 del curso, y es hora de seguir un paso más adelante con nuestro viaje a través de las Tierras del Machine Learning. Nos veremos en la próxima: