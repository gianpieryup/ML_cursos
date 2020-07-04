# Importar el dataset
dataset = read.csv('Data.csv')


# Tratamiento de los valores NA
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)


# Codificar las variables categóricas
# "levels" => sera marcado como "labels"
dataset$Country = factor(dataset$Country,
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1, 2, 3))

 
dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0,1))
# Recordar que Los indices de R empiezan con 1





# Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools") # Solo una ves
library(caTools) # Correr esta linea o marcar el check

set.seed(123) # Configurar semilla
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# SplitRatio : %de entrenamiento

# > split
# [1]  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE  TRUE FALSE  TRUE

training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)




# Escalado de valores
training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])

# No escalo el "Pais" y "Puncharse" por que no son numeros(es otro tipo de dato,labels) y R no puede compararlos con numeros