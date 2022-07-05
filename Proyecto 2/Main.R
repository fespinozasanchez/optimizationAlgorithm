library(readr)
library(patchwork)
require(pacman)
pacman::p_load(raster, ggplot2, sf, tidyverse)


# Parliaments of 20 Members ----------------------------------------------
Matriz20 <- read_csv("Matriz20.csv", col_types = cols(...1 = col_skip()))
names(Matriz20) = c("x","y")
# Parliaments of 50 Members ----------------------------------------------
Matriz50 <- read_csv("Matriz50.csv", col_types = cols(...1 = col_skip()))
names(Matriz50) = c("x","y")


# PLOT 20 | 50 MEMBERS ----------------------------------------------------
plotMatriz20 = qplot(data=Matriz20, x=x, y= y)+ 
  geom_point(size=3,colour='blue')+
  ggtitle("20 Members")+ 
  facet_grid()
plotMatriz50 = qplot(data=Matriz50, x=x, y= y)+ 
  geom_point(size=3,colour='red')+
  ggtitle("50 Members")+
  facet_grid()

plotMatriz20 | plotMatriz50


# -------------------------------------------------------------------------



# Function That Generates Distance Matrix of Points ------------------------------------------

matriz_Distance <- function(MatrizN){
  coordinates(MatrizN) <- ~ x + y
  return (pointDistance(MatrizN, lonlat=FALSE))
}

dists20 <- matriz_Distance(Matriz20)
dists50 <- matriz_Distance(Matriz50)


dists20
dists50


# Function to generate n vectors in a matrix ------------------------------------------------------
matriz_Generate <- function(ncols, nrows, prob,sizes,ranges){
  return (matrix(rbinom( sizes, ranges, prob), nrow=nrows, ncol = ncols[1]))
}

ncols = sample(60:80,replace=T)
nrows = 20
prob = .4
matriz_gen20 =  matriz_Generate(ncols,nrows,prob,(ncols[1]*nrows),1)

matriz_gen20


# Condition ---------------------------------------------------------------

#while(sum(dataSorted == dataSorted[best])<length(matriz_gen20)/2+1){
 # print("hola")
#}




# Distances Sum ----------------------------------------------------------
generic_Acummulate <- function(matriz,dists){
  data = c()
  for (i in 1:ncol(matriz)){
    acumulate = 0
    pos <- which(matriz[,i]==1)
      for(j in 1:length(pos)){
        for(k in 1:length(pos)-1){
         acumulate=acumulate+dists20[pos[j],pos[k+1]]
        }
      }
    
    data <-c(data,acumulate)
   
  }

  return (data/sum(data))
}

data = generic_Acummulate(matriz_gen20, dists20)
sum(data)
#FINAL DE ALGORITMO PARA MOSTRAR PUNTOS EN ORDEN
dataSorted=sort(data,decreasing = T)
best=which.max(dataSorted)
best
sum(dataSorted == dataSorted[best])

# Best Prob ---------------------------------------------------------------

best_vector <- function(matriz, best){
  return (c(matriz_gen20[,best]))
}


b_vector = best_vector(matriz_gen20,best) 
b_vector


# Selection ---------------------------------------------------------------
bestC=which.max(data)
oldPop<- matriz_gen20[, -bestC]
newPop=oldPop

for(i in 1:ncol(oldPop)){
  random_selection= sample(1:ncol(oldPop),3,replace=F)
  max=0
  for (i in random_selection){
    if(data[i]>max){
      max=i
      }
  }
  newPop[,i]=oldPop[,max]
  
}


#Crossover ----------------------------------------------------------------
for (i in 1:ncol(newPop)) {
  chromosome = c()
  for (j in ncol(newPop):1){
    genP1 = newPop[,i][1:((length(newPop[,i])/2)+1)]
    genP2 = newPop[,j][((length(newPop[,i])/2)+2):length(newPop[,j])]
    chromosome = c(genP1,genP2)
    
  }
  newPop[,i] =chromosome
}

newPop

# Mutation ----------------------------------------------------------------


