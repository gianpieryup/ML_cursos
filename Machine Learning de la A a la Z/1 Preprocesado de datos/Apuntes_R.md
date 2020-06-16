## Pre-procesado en R

**Antes de todo** : Fija que estés parado en el directorio de trabajo

Para cargar la librería (`package`) en R, existen dos formas: La primera es en lineá de comandos

 ````R
library(nombre_paquete)
 ````

La segunda mas usada, es tildar con un **check** al paquete en la sección `packages` de la derecha, esto equivale a escribir la lineá de comandos de arriba

![packages_R](packages_R.png)

> Ojo: no estamos instalando (algo nuevo) sino cargando paquetes que ya vienen en R. Los cargamos al proyecto para poder usarlos

````R
# Importar el dataset
dataset = read.csv('Data.csv')
# NO es necesario separar los DEP y los IND

````

