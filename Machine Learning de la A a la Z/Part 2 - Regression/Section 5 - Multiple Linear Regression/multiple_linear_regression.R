# Regresión Lineal Multiple

# Importar el dataset
dataset = read.csv('50_Startups.csv')
#dataset = dataset[, 2:3]

# Codificar las variables categoricas
dataset$State = factor(dataset$State,
                         levels = c("New York", "California", "Florida"),
                         labels = c(1, 2, 3))



# Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Ajustar el modelo de Regresion Lineal Multiple con el Conjunto de Entrenamiento
regression = lm(formula = Profit ~ .,
                data = training_set)
#La notacion (.) quiere decir todo lo demas, del [data=training_Set]
#Automaticamente convierte a dummy y corta uno (R papa)
#USar summary para ver la info

# Predecir los resultados con el conjunto de testing
y_pred = predict(regression, newdata = testing_set)



# Construir un modelo optimo con la Eliminacion hacia atras
SL = 0.05
regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
                data = dataset)
summary(regression)

#El "state 2 y 3" tenian "~0.990" por lo que se elimino 'State' de donde vienen

regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend,
                data = dataset)
summary(regression)
