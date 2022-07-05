library(readr)
library(patchwork)
require(pacman)
pacman::p_load(raster, ggplot2, sf, tidyverse)
options(max.print=999999)

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


# Function to generate n vectors in a matrix ------------------------------------------------------
matriz_Generate <- function(ncols, nrows, prob,sizes,ranges){
  return (matrix(rbinom( sizes, ranges, prob), nrow=nrows, ncol = ncols[1]))
}

ncols = sample(60:80,replace=T)
nrows = 20
prob = .4
matriz_gen20 =  matriz_Generate(ncols,nrows,prob,(ncols[1]*nrows),1)

# Condition ---------------------------------------------------------------

#while(sum(dataSorted == dataSorted[best])<length(matriz_gen20)/2+1){
 # print("hola")
#}




# Distances Sum ----------------------------------------------------------
generic_Acummulate <- function(matriz, dists){
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

data_20 = generic_Acummulate(matriz_gen20, dists20)


# Selection ---------------------------------------------------------------
Selection <- function(data, matriz){
  bestC=which.max(data)
  oldPop = matriz[, -bestC]
  newPop=oldPop
  for(i in 1:ncol(oldPop)){
    random_selection= sample(1:ncol(oldPop),3,replace=F)
    max=0
    for (i in random_selection){
      if(data[i] > max){
        max=i
      }
      newPop[,i]=oldPop[,max]
    }
  }
  return(newPop)
  
}

newPop_20 = Selection(data_20, matriz_gen20)


#Crossover ----------------------------------------------------------------
Crossover <- function(newPop){
  cross_Pop = matrix(nrow = nrow(newPop),ncol = ncol(newPop))
  i=1
  while(i < ncol(newPop)){
    if (ncol(newPop) %% 2 == 0){
      genP1 <- newPop[,i][1:((nrow(newPop)/2)+1)]
      genP2 <- newPop[,i+1][((nrow(newPop)/2)+2):nrow(newPop)]
      cross_Pop[,i] = c(genP1,genP2)
      cross_Pop[,i+1] = c(genP2,genP1)
      i = i + 1
    }else{
      if(i<ncol(newPop)){
        genP1 <- newPop[,i][1:((nrow(newPop)/2)+1)]
        genP2 <- newPop[,i+1][((nrow(newPop)/2)+2):nrow(newPop)]
        cross_Pop[,i] = c(genP1,genP2)
        cross_Pop[,i+1] = c(genP2,genP1)
        i = i + 1
      }else{
        if(i==ncol(newPop)){
          genP1 <- newPop[,i][1:((nrow(newPop)/2)+1)]
          genP2 <- newPop[,i][((nrow(newPop)/2)+2):nrow(newPop)]
          chromosomeh2 = c(genP2,genP1)
          cross_Pop[,i] = chromosomeh2
          break
        }
      }
      
    }
  }
  return (cross_Pop)
  
}
cross_Pop_20 = Crossover(newPop_20)

# Mutation ----------------------------------------------------------------
Mutation <- function(matriz, vector_best){
  for(i in  1:ncol(matriz)){
    random_gen=sample(1:20,1)
    if(runif(1)>0.60){
      matriz[,i][random_gen] <- ifelse(matriz[,i][random_gen]==1, 0, 1)
    }
  }
  matriz = cbind(matriz,vector_best[,bestC])
  return (matriz)
}




Mutation_20 = Mutation(cross_Pop_20, matriz_gen20)


# Chart Chromosome --------------------------------------------------------


chromosome_Chart <- function(nsize, porc){
  best = porc[which.max(porc)]
  label = c()
  for (j in 1:nsize) {
    n_chromosome = paste("C",j)
    label <-c(label,n_chromosome)
    
  }
  print(label)
  print(porc)
  label <- paste(label,": ")
  label <- paste(label, porc)
  label <- paste(label, "%", sep = "")
  pie(porc, main = "Percentage of each chromosome",sub = paste("best:",best) , col = rainbow(10))
  legend("topleft", legend =label,fill = rainbow(10))
}

chromosome_Chart(length(data), data)


  



#FINAL DE ALGORITMO PARA MOSTRAR PUNTOS EN ORDEN
dataSorted=sort(data,decreasing = T)
best=which.max(dataSorted)
best
sum(dataSorted == dataSorted[best])

