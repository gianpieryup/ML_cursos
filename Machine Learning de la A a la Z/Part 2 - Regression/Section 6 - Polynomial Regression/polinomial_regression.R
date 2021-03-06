# Regresión Polinómica

# Importar el dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[, 2:3]

# Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools")
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# testing_set = subset(dataset, split == FALSE)


# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])


# ------------ AJustes -------------------------------
# Ajustar Modelo de Regresion Lineal con el Conjunto de Datos
lin_reg = lm(formula = Salary ~ ., 
             data = dataset)

# Ajustar Modelo de Regresion Polinomica con el Conjunto de Datos
# COMO EN ECN CREAMOS LA MATRIZ A de Ax=b
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula = Salary ~ .,
              data = dataset)



# Visualizacion del modelo lineal
# install.packages("ggplot2")
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)),
            color = "blue") +
  ggtitle("Prediccion lineal del sueldo en funcion del nivel del empleado") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")


# Visualizacion del modelo polinomico
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(poly_reg, 
                                        newdata = data.frame(Level = x_grid,
                                                             Level2 = x_grid^2,
                                                             Level3 = x_grid^3,
                                                             Level4 = x_grid^4))),
            color = "blue") +
  ggtitle("Prediccion polinomica del suedlo en funcion del nivel del empleado") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")



# Prediccion de nuevos resultados con Regresión Lineal
# predict(MODELO, newdata = DATAFRAME) NO OLVIDAR QUE DEBEN COINCIDIR LOS NOMBRES DE LAS COLUMNAS DEL DATAFRAME CON LOS DEL MODELO CONSTRUIDO
y_pred = predict(lin_reg, newdata = data.frame(Level = 6.5))

# Prediccion de nuevos resultados con Regresion Polinomica
# TANTO EN ESTE COMO EN EL ANTERIOR SE DEBEN PASAR DATAFRAME COMO PARAMETRO EN "newdata" en python son arrays
y_pred_poly = predict(poly_reg, newdata = data.frame(Level = 6.5,
                                                Level2 = 6.5^2,
                                                Level3 = 6.5^3,
                                                Level4 = 6.5^4))


