library(tidyverse)
library(readr)
library(ggplot2)
library(patchwork)
require(pacman)
pacman::p_load(raster, hablar, rgdal, rgeos, sna, foreign, stringr, sf, tidyverse, gtools)


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


# Distance between points -------------------------------------------------

coordinates(Matriz20) <- ~ x + y
coordinates(Matriz50) <- ~ x + y
dists20 <- pointDistance(Matriz20, lonlat=FALSE)
dists50 <- pointDistance(Matriz50, lonlat=FALSE)


dists20
dists50

# -------------------------------------------------------------------------


