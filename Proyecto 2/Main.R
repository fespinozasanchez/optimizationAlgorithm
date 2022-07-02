library(tidyverse)
library(readr)
library(ggplot2)
library(patchwork)
#install.packages('patchwork')



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




# suma <- function(x, y) {
#   return(c(x,y))
# }
# 
# 
# suma(1,2)
