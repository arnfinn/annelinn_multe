library(dplyr)
library(tidyr)
library(DT)
library(xtable)


database <<- read.table('samla_analyser.csv', sep = ";", header=T, encoding = 'UTF-8', stringsAsFactors = FALSE)

tmp <- database %>% group_by(Clone, Year, Season)

tmp$dates <- tmp$Harvest_date %>% as.Date("%d.%m.%y")

ta <- tmp %>% summarise(verdi=mean(TA))
tp <- tmp %>% summarise(verdi=mean(TP))
ea <- tmp %>% summarise(verdi=mean(EA))
ms <- tmp %>% summarise(verdi=mean(MS))
