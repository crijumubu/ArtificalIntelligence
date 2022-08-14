#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from scipy import stats

file = 'abalone.csv'

data = pd.read_csv(file)

# First method

data.columns = ["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"]

# Definicion de funciones

def errorWindow(message):
    newgraphWindow = tk.Toplevel(root)
    newgraphWindow.resizable(False, False)
    newgraphWindow.title('Error')
    
    frame = tk.Frame(newgraphWindow, width='1080', height='650')
    frame.pack()
    frame['bg'] = '#faf9f9' 
    
    lbl = tk.Label(frame, text=message, bg='#faf9f9', font=(16))
    lbl.grid(row=0)
    
    btnClose = tk.Button(frame, text="Cerrar", activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2', command=lambda: newgraphWindow.destroy())
    btnClose.grid(row=1, pady=10)

def checkSelectedInput():
    selectedInput = []
    
    if varInputLenght.get() == 1:
        selectedInput.append('Length')
    if varInputDiameter.get() == 1:
        selectedInput.append('Diameter')
    if varInputHeight.get() == 1:
        selectedInput.append('Height')
    if varInputWholeWeight.get() == 1:
        selectedInput.append('Whole weight')
    if varInputShuckedWeight.get() == 1:
        selectedInput.append('Shucked weight')
    if varInputVisceraWeight.get() == 1:
        selectedInput.append('Viscera weight')
    if varInputShellWeight.get() == 1:
        selectedInput.append('Shell weight')
    if varInputRings.get() == 1:
        selectedInput.append('Rings')
    
    return selectedInput

def graph():
    
    selectedInput = checkSelectedInput()
    
    if (comboGraphs.get() == 'Histograma'):
        if (len(selectedInput) == 1):
            plot.hist(data[selectedInput[0]])
            plot.title(selectedInput[0])
            plot.xlabel('Valor de los datos')
            plot.ylabel('Cantidad de los datos')
            plot.show()
        else:
            errorWindow('Para graficar un histograma se requiere que \n únicamente tengas una variable de entrada seleccionada ')

# Definicion del root

root = tk.Tk()

root.title('Abalone')
root.resizable(False, False)

# Definicion del frame

frame = tk.Frame(root, width='1080', height='650')
frame.pack()
frame['bg'] = '#faf9f9'

# Titulo principal

title = tk.Label(frame, text='Abalone Data Analysys', bg='#faf9f9', font=(16))
title.grid(column=1, columnspan=2, sticky='NWES', pady=10)

# Tipo de graficas, definicion del estilo y despliegue de combobox

comboLabel = tk.Label(frame, text='Tipo de gráfica:', bg='#faf9f9')
comboLabel.grid(row=1, column=0, sticky='W', pady=10)

comboStyle = ttk.Style()
comboStyle.theme_create(
    'combostyle', parent = 'alt',
    settings = {'TCombobox':
                {'configure':
                 {'selectbackground': '#555B6E',
                  'fieldbackground': '#555B6E',
                  'background': '#555B6E',
                  }}}
)

comboStyle.theme_use('combostyle') 

comboGraphs = ttk.Combobox(
    frame,
    state='readonly',
    values=['Histograma','Diagrama de caja','Disperción','Normalización']    
)

comboGraphs.config(foreground='#faf9f9')
comboGraphs.current(0)
comboGraphs.grid(row=1, column=1, sticky='E', pady=15)

# Variables de entrada, seleccion de las multiples variables de entrada

varLabel = tk.Label(frame, text='Variables de entrada:', bg='#faf9f9')
varLabel.grid(row=2, column=0, sticky='W')

varInputLenght = tk.IntVar()
varInputDiameter = tk.IntVar()
varInputHeight = tk.IntVar()
varInputWholeWeight = tk.IntVar()
varInputShuckedWeight = tk.IntVar()
varInputVisceraWeight = tk.IntVar()
varInputShellWeight = tk.IntVar()
varInputRings = tk.IntVar()

chkbtnInputLenght = tk.Checkbutton(frame, text=' Longitud', bg='#faf9f9', highlightbackground = '#faf9f9', activebackground='#faf9f9', variable=varInputLenght, onvalue=1, offvalue=0,)
chkbtnInputLenght.grid(row=2, column=1, sticky='W')

chkbtnInputDiameter = tk.Checkbutton(frame, text=' Diametro', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputDiameter, onvalue=1, offvalue=0,)
chkbtnInputDiameter.grid(row=2, column=2, sticky='W')

chkbtnInputHeight = tk.Checkbutton(frame, text=' Altura', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputHeight, onvalue=1, offvalue=0,)
chkbtnInputHeight.grid(row=2, column=3, sticky='W')

chkbtnInputWholeWeight = tk.Checkbutton(frame, text=' Peso completo', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputWholeWeight, onvalue=1, offvalue=0,)
chkbtnInputWholeWeight.grid(row=3, column=1, sticky='W')

chkbtnInputShuckedWeight = tk.Checkbutton(frame, text=' Peso de la concha', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputShuckedWeight, onvalue=1, offvalue=0,)
chkbtnInputShuckedWeight.grid(row=3, column=2, sticky='W')

chkbtnInputVisceraWeight = tk.Checkbutton(frame, text=' Peso de la víscera', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputVisceraWeight, onvalue=1, offvalue=0,)
chkbtnInputVisceraWeight.grid(row=3, column=3, sticky='W')

chkbtnInputShellWeight = tk.Checkbutton(frame, text=' Peso del caparazón', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputShellWeight, onvalue=1, offvalue=0,)
chkbtnInputShellWeight.grid(row=4, column=1, sticky='W')

chkbtnInputRings = tk.Checkbutton(frame, text=' Número de anillos', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRings, onvalue=1, offvalue=0,)
chkbtnInputRings.grid(row=4, column=2, sticky='W')

# Atipicos

atipicLabel = tk.Label(frame, text='Valor del factor de alpha para los atípicos:', bg='#faf9f9')
atipicLabel.grid(row=5, column=0, columnspan=2, sticky='NW', pady=15)

atipicInput = ttk.Entry(frame)
atipicInput.grid(row=5, column=2, sticky='W', padx=10)

btnAtipic = tk.Button(frame, text='Eliminar atípicos', activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2')
btnAtipic.grid(row=5, column=3, pady=15)

# Entradas de la regresion

regressionLabel = tk.Label(frame, text='Entradas de la regresión:', bg='#faf9f9')
regressionLabel.grid(row=6, column=0, sticky='W')

varInputRegressionLenght = tk.IntVar()
varInputRegressionDiameter = tk.IntVar()
varInputRegressionHeight = tk.IntVar()
varInputRegressionWholeWeight = tk.IntVar()
varInputRegressionShuckedWeight = tk.IntVar()
varInputRegressionVisceraWeight = tk.IntVar()
varInputRegressionShellWeight = tk.IntVar()
varInputRegressionRings = tk.IntVar()

chkbtnInputRegressionLenght = tk.Checkbutton(frame, text=' Longitud', bg='#faf9f9', highlightbackground = '#faf9f9', activebackground='#faf9f9', variable=varInputRegressionLenght, onvalue=1, offvalue=0,)
chkbtnInputRegressionLenght.grid(row=6, column=1, sticky='W')

chkbtnInputRegressionDiameter = tk.Checkbutton(frame, text=' Diametro', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionDiameter, onvalue=1, offvalue=0,)
chkbtnInputRegressionDiameter.grid(row=6, column=2, sticky='W')

chkbtnInputRegressionHeight = tk.Checkbutton(frame, text=' Altura', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionHeight, onvalue=1, offvalue=0,)
chkbtnInputRegressionHeight.grid(row=6, column=3, sticky='W')

chkbtnInputRegressionWholeWeight = tk.Checkbutton(frame, text=' Peso completo', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionWholeWeight, onvalue=1, offvalue=0,)
chkbtnInputRegressionWholeWeight.grid(row=7, column=1, sticky='W')

chkbtnInputRegressionShuckedWeight = tk.Checkbutton(frame, text=' Peso de la concha', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionShuckedWeight, onvalue=1, offvalue=0,)
chkbtnInputRegressionShuckedWeight.grid(row=7, column=2, sticky='W')

chkbtnInputRegressionVisceraWeight = tk.Checkbutton(frame, text=' Peso de la víscera', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionVisceraWeight, onvalue=1, offvalue=0,)
chkbtnInputRegressionVisceraWeight.grid(row=7, column=3, sticky='W')

chkbtnInputRegressionShellWeight = tk.Checkbutton(frame, text=' Peso del caparazón', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionShellWeight, onvalue=1, offvalue=0,)
chkbtnInputRegressionShellWeight.grid(row=8, column=1, sticky='W', pady=(0,15))

chkbtnInputRegressionRings = tk.Checkbutton(frame, text=' Número de anillos', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionRings, onvalue=1, offvalue=0,)
chkbtnInputRegressionRings.grid(row=8, column=2, sticky='W', pady=(0,15))

# Salidas de la regresion

regressionLabel = tk.Label(frame, text='Salidas de la regresión:', bg='#faf9f9')
regressionLabel.grid(row=9, column=0, sticky='W')

varOutputRegressionLenght = tk.IntVar()
varOutputRegressionDiameter = tk.IntVar()
varOutputRegressionHeight = tk.IntVar()
varOutputRegressionWholeWeight = tk.IntVar()
varOutputRegressionShuckedWeight = tk.IntVar()
varOutputRegressionVisceraWeight = tk.IntVar()
varOutputRegressionShellWeight = tk.IntVar()
varOutputRegressionRings = tk.IntVar()

chkbtnOutputRegressionLenght = tk.Checkbutton(frame, text=' Longitud', bg='#faf9f9', highlightbackground = '#faf9f9', activebackground='#faf9f9', variable=varOutputRegressionLenght, onvalue=1, offvalue=0,)
chkbtnOutputRegressionLenght.grid(row=9, column=1, sticky='W')

chkbtnOutputRegressionDiameter = tk.Checkbutton(frame, text=' Diametro', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionDiameter, onvalue=1, offvalue=0,)
chkbtnOutputRegressionDiameter.grid(row=9, column=2, sticky='W')

chkbtnOutputRegressionHeight = tk.Checkbutton(frame, text=' Altura', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionHeight, onvalue=1, offvalue=0,)
chkbtnOutputRegressionHeight.grid(row=9, column=3, sticky='W')

chkbtnOutputRegressionWholeWeight = tk.Checkbutton(frame, text=' Peso completo', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionWholeWeight, onvalue=1, offvalue=0,)
chkbtnOutputRegressionWholeWeight.grid(row=10, column=1, sticky='W')

chkbtnOutputRegressionShuckedWeight = tk.Checkbutton(frame, text=' Peso de la concha', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionShuckedWeight, onvalue=1, offvalue=0,)
chkbtnOutputRegressionShuckedWeight.grid(row=10, column=2, sticky='W')

chkbtnOutputRegressionVisceraWeight = tk.Checkbutton(frame, text=' Peso de la víscera', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionVisceraWeight, onvalue=1, offvalue=0,)
chkbtnOutputRegressionVisceraWeight.grid(row=10, column=3, sticky='W')

chkbtnOutputRegressionShellWeight = tk.Checkbutton(frame, text=' Peso del caparazón', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionShellWeight, onvalue=1, offvalue=0,)
chkbtnOutputRegressionShellWeight.grid(row=11, column=1, sticky='W')

chkbtnOutputRegressionRings = tk.Checkbutton(frame, text=' Número de anillos', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionRings, onvalue=1, offvalue=0,)
chkbtnOutputRegressionRings.grid(row=11, column=2, sticky='W')

# Boton de realizar la regresion

btnregression = tk.Button(frame, text='Obtener regresión', activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2')
btnregression.grid(row=12, column=1, sticky='WE', padx=5, pady=10)

# Boton de graficar

btngraph = tk.Button(frame, text='Graficar', activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2', command=graph)
btngraph.grid(row=12, column=2, sticky='WE', padx=5, pady=10)

# Espera a la accion

root.mainloop()