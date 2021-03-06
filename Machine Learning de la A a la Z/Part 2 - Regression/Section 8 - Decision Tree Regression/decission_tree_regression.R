# Árbol de Decisión para Regresión

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


# Ajustar Modelo de Regresión con el Conjunto de Datos
# install.packages("rpart") # Libreria de Arboles de Desicion
library(rpart)
regression = rpart(formula = Salary ~ .,
                   data = dataset,
                   control = rpart.control(minsplit = 1))
# control = "Se seguira dividiendo si la hoja tiene mas de 1 elemento"
# -------------

# Predicción de nuevos resultados con Árbol Regresión 
y_pred = predict(regression, newdata = data.frame(Level = 6.5))



# Visualización del modelo de árbol de regresión
# install.packages("ggplot2")
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression, 
                                        newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("Predicción con Árbol de Decisión (Modelo de Regresión)") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")
