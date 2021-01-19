# Apriori

# Preprocesado de Datos
# install.packages("arules")
library(arules) 
library(arulesViz)

dataset = read.csv("Market_Basket_Optimisation.csv", header = FALSE) # (header) tiene valor simbolico
dataset = read.transactions("Market_Basket_Optimisation.csv",
                            sep = ",", rm.duplicates = TRUE) # Transformarlo a matriz usuario/Productos con un valor de 0 Û 1 en cada casilla/ Ademas quita el duplicado
summary(dataset)
# density of 0.03288973 significa que el 99% son 'ceros'

itemFrequencyPlot(dataset, topN = 10)


# Entrenar algoritmo Apriori con el dataset
rules = apriori(data = dataset, 
                parameter = list(support = 0.004, confidence = 0.2))

# 3*7/7500  esto quiere decir que el producto se vendio al menos 3 veces en el dia en una semana(el dataset es de 1 semana)
# El 0.8 nos lo recomienda y esta por defecto en R

  
# Visualizaci√≥n de los resultados
inspect(sort(rules, by = 'lift')[1:10])
  
plot(rules, method = "graph", engine = "htmlwidget")


  