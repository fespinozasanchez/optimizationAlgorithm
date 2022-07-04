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

ncols = sample(3:5,replace=T)
nrows = 20
prob = .4
matriz_gen20 =  matriz_Generate(ncols,nrows,prob,(ncols[1]*nrows),1)

matriz_gen20
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
data
sum(data)













