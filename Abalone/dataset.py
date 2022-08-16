#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importacion de bibliotecas y paquetes necesarios para la ejecucion del aplicativo

import pandas as pd

# Definicion de la clase para el dataset

class dataSet():

    fileRelativeRoute = ''

    data = pd.DataFrame()

    copyData = pd.DataFrame()

    def __init__(self, fileRoute):
        
        self.fileRelativeRoute = fileRoute

        self.data = pd.read_csv(self.fileRelativeRoute)

        self.copyData = pd.read_csv(self.fileRelativeRoute)

    def setColums(self, listColumns):

        self.data.columns = listColumns
        self.copyData.columns = listColumns

    def getColumns(self):
        return self.data.columns