## Bienvenido a la Parte 5 - Reglas de Asociación



Bienvenidos a la Parte 5 - Aprendizaje con Reglas de Asociación



Los clientes que lo compraron, también compraron... De esto va el tema de Aprendizaje con Reglas de Asociación!

En esta parte, vamos a aprender a implementar dos modelos de reglas de asociación:

1. **Apriori**
2. **Eclat**



¡Disfruta del Machine Learning como siempre!



### Recurso adicional: cómo representar las reglas de asociación en un grafo

Os dejo a continuación un ejemplo de como representar las reglas de asociación cortesía de un alumno del curso. Gracias poor compartirlo!!

```R
# ------------------------------------------------------------------------
# GOAL: show how to create html widgets with transaction rules
# ------------------------------------------------------------------------
 
# libraries --------------------------------------------------------------
library(arules)
library(arulesViz)
 
# data -------------------------------------------------------------------
path <- "~/Downloads/P14-Part5-Association-Rule-Learning/Section 28 - Apriori/"
trans <- read.transactions(
file = paste0(path, "R/Market_Basket_Optimisation.csv"),
sep = ",",
rm.duplicates = TRUE
)
 
# apriori algoirthm ------------------------------------------------------
rules <- apriori(
data = trans,
parameter = list(support = 0.004, confidence = 0.2)
)
 
# visualizations ---------------------------------------------------------
plot(rules, method = "graph", engine = "htmlwidget")
```