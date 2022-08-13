#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from scipy import stats

file = 'abalone.csv'

data = pd.read_csv(file)

# First method

data.columns = ["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"]

''' 
Second method -> Add the index row at the first line of the dataset
'''

# Generate graphics

plot.hist(x=data["Length"])
plot.title("Histograma de la segunda columna")
plot.xlabel("Valor de los datos")
plot.ylabel("Cantidad de los datos")

plot.subplots()
plot.boxplot(x=data["Length"])

graph = plot.figure()
ax = graph.add_subplot(111)
res = stats.probplot(data["Length"], dist=stats.norm, sparams=(6,), plot=ax)

plot.subplots()
plot.scatter(data["Length"], data["Diameter"])

# Correlation graph

correlation = data.corr()
print(correlation)