#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importacion de bibliotecas y paquetes necesarios para la ejecucion del aplicativo

import matplotlib.pyplot as plot
import tkinter as tk
import numpy as np
import dataSet as ds
from tkinter import END, ttk
from scipy import stats

# Definicion de la clase de la aplicacion

class main():
    
    # Importacion del dataset del abalone mediante la creacion de un objeto de la clase DataSet

    dataSetObject = ds.dataSet('Abalone/abalone.csv')
    dataSetObject.setColums(["Sex", "Length", "Diameter", "Height", "Whole weight", "Shucked weight", "Viscera weight", "Shell weight", "Rings"])

    # Definicion del root y del frame

    root = tk.Tk()
    frame = tk.Frame(root, width='1080', height='650')

    # Titulo principal

    title = tk.Label(frame, text='Abalone Data Analysys', bg='#faf9f9', font=(16))

    # Despliegue del tipo de graficas

    comboLabel = tk.Label(frame, text='Tipo de gráfica:', bg='#faf9f9')
    comboStyle = ttk.Style()
    comboGraphs = ttk.Combobox(
    frame,
    state='readonly',
    values=['Histograma','Diagrama de caja','Dispersión','Normalización']    
    )

    # Definicion de las variables de entrada y los campos de seleccion

    varLabel = tk.Label(frame, text='Variables de entrada:', bg='#faf9f9')

    varInputLenght = tk.IntVar()
    varInputDiameter = tk.IntVar()
    varInputHeight = tk.IntVar()
    varInputWholeWeight = tk.IntVar()
    varInputShuckedWeight = tk.IntVar()
    varInputVisceraWeight = tk.IntVar()
    varInputShellWeight = tk.IntVar()
    varInputRings = tk.IntVar()

    chkbtnInputLenght = tk.Checkbutton(frame, text=' Longitud', bg='#faf9f9', highlightbackground = '#faf9f9', activebackground='#faf9f9', variable=varInputLenght, onvalue=1, offvalue=0)
    chkbtnInputDiameter = tk.Checkbutton(frame, text=' Diametro', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputDiameter, onvalue=1, offvalue=0)
    chkbtnInputHeight = tk.Checkbutton(frame, text=' Altura', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputHeight, onvalue=1, offvalue=0)
    chkbtnInputWholeWeight = tk.Checkbutton(frame, text=' Peso completo', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputWholeWeight, onvalue=1, offvalue=0)    
    chkbtnInputShuckedWeight = tk.Checkbutton(frame, text=' Peso de la concha', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputShuckedWeight, onvalue=1, offvalue=0)
    chkbtnInputVisceraWeight = tk.Checkbutton(frame, text=' Peso de la víscera', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputVisceraWeight, onvalue=1, offvalue=0)
    chkbtnInputShellWeight = tk.Checkbutton(frame, text=' Peso del caparazón', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputShellWeight, onvalue=1, offvalue=0)
    chkbtnInputRings = tk.Checkbutton(frame, text=' Número de anillos', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRings, onvalue=1, offvalue=0)

    # Datos atipicos

    atypicalLabel = tk.Label(frame, text='Valor del factor de alpha para los atípicos:', bg='#faf9f9')
    atypicalInput = ttk.Entry(frame)
    btnAtypical = tk.Button(frame, text='Eliminar atípicos', activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2')

    # Regresion

    regressionLabel = tk.Label(frame, text='Entradas de la regresión:', bg='#faf9f9')

    # Definicion de las variables de entrada y los campos de seleccion para la regresion

    varInputRegressionLenght = tk.IntVar()
    varInputRegressionDiameter = tk.IntVar()
    varInputRegressionHeight = tk.IntVar()
    varInputRegressionWholeWeight = tk.IntVar()
    varInputRegressionShuckedWeight = tk.IntVar()
    varInputRegressionVisceraWeight = tk.IntVar()
    varInputRegressionShellWeight = tk.IntVar()
    varInputRegressionRings = tk.IntVar()

    chkbtnInputRegressionLenght = tk.Checkbutton(frame, text=' Longitud', bg='#faf9f9', highlightbackground = '#faf9f9', activebackground='#faf9f9', variable=varInputRegressionLenght, onvalue=1, offvalue=0)
    chkbtnInputRegressionDiameter = tk.Checkbutton(frame, text=' Diametro', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionDiameter, onvalue=1, offvalue=0)
    chkbtnInputRegressionHeight = tk.Checkbutton(frame, text=' Altura', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionHeight, onvalue=1, offvalue=0)
    chkbtnInputRegressionWholeWeight = tk.Checkbutton(frame, text=' Peso completo', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionWholeWeight, onvalue=1, offvalue=0)
    chkbtnInputRegressionShuckedWeight = tk.Checkbutton(frame, text=' Peso de la concha', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionShuckedWeight, onvalue=1, offvalue=0)
    chkbtnInputRegressionVisceraWeight = tk.Checkbutton(frame, text=' Peso de la víscera', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionVisceraWeight, onvalue=1, offvalue=0)
    chkbtnInputRegressionShellWeight = tk.Checkbutton(frame, text=' Peso del caparazón', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionShellWeight, onvalue=1, offvalue=0)
    chkbtnInputRegressionRings = tk.Checkbutton(frame, text=' Número de anillos', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varInputRegressionRings, onvalue=1, offvalue=0)

    # Definicion de las variables de salida y los campos de seleccion para la regresion

    regressionLabel = tk.Label(frame, text='Salidas de la regresión:', bg='#faf9f9')
    varOutputRegressionLenght = tk.IntVar()
    varOutputRegressionDiameter = tk.IntVar()
    varOutputRegressionHeight = tk.IntVar()
    varOutputRegressionWholeWeight = tk.IntVar()
    varOutputRegressionShuckedWeight = tk.IntVar()
    varOutputRegressionVisceraWeight = tk.IntVar()
    varOutputRegressionShellWeight = tk.IntVar()
    varOutputRegressionRings = tk.IntVar()

    chkbtnOutputRegressionLenght = tk.Checkbutton(frame, text=' Longitud', bg='#faf9f9', highlightbackground = '#faf9f9', activebackground='#faf9f9', variable=varOutputRegressionLenght, onvalue=1, offvalue=0)
    chkbtnOutputRegressionDiameter = tk.Checkbutton(frame, text=' Diametro', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionDiameter, onvalue=1, offvalue=0)
    chkbtnOutputRegressionHeight = tk.Checkbutton(frame, text=' Altura', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionHeight, onvalue=1, offvalue=0)
    chkbtnOutputRegressionWholeWeight = tk.Checkbutton(frame, text=' Peso completo', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionWholeWeight, onvalue=1, offvalue=0)
    chkbtnOutputRegressionShuckedWeight = tk.Checkbutton(frame, text=' Peso de la concha', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionShuckedWeight, onvalue=1, offvalue=0)
    chkbtnOutputRegressionVisceraWeight = tk.Checkbutton(frame, text=' Peso de la víscera', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionVisceraWeight, onvalue=1, offvalue=0)
    chkbtnOutputRegressionShellWeight = tk.Checkbutton(frame, text=' Peso del caparazón', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionShellWeight, onvalue=1, offvalue=0)
    chkbtnOutputRegressionRings = tk.Checkbutton(frame, text=' Número de anillos', highlightbackground = '#faf9f9', activebackground='#faf9f9', bg='#faf9f9', variable=varOutputRegressionRings, onvalue=1, offvalue=0)

    # Definicion del boton de realizar la regresion
    
    btnregression = tk.Button(frame, text='Obtener regresión', activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2')

    # Definicion del boton de graficar

    btngraph = tk.Button(frame, text='Graficar', activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2')

    def __init__(self):
        super().__init__()

        # Modificacion de propiedades del root

        self.root.title('Abalone')
        self.root.resizable(False, False)   

        # Modificacion de propiedades del frame

        self.frame.pack()
        self.frame['bg'] = '#faf9f9'

        # Titulo principal - Ubicacion en el grid

        self.title.grid(column=1, columnspan=2, sticky='NWES', pady=10)

        # Tipo de graficas, definicion del estilo, despliegue de combobox y ubicacion en el grid

        self.comboLabel.grid(row=1, column=0, sticky='W', pady=10)

        self.comboStyle.theme_create(
            'combostyle', parent = 'alt',
            settings = {'TCombobox':
                        {'configure':
                        {'selectbackground': '#555B6E',
                        'fieldbackground': '#555B6E',
                        'background': '#555B6E',
                        }}}
        )

        self.comboStyle.theme_use('combostyle') 

        self.comboGraphs.config(foreground='#faf9f9')
        self.comboGraphs.current(0)
        self.comboGraphs.grid(row=1, column=1, sticky='E', pady=15)

        # Variables de entrada y seleccion de los campos para las mismas - Ubicacion en el grid

        self.varLabel.grid(row=2, column=0, sticky='W')

        self.chkbtnInputLenght.grid(row=2, column=1, sticky='W')
        self.chkbtnInputDiameter.grid(row=2, column=2, sticky='W')
        self.chkbtnInputHeight.grid(row=2, column=3, sticky='W')
        self.chkbtnInputWholeWeight.grid(row=3, column=1, sticky='W')
        self.chkbtnInputShuckedWeight.grid(row=3, column=2, sticky='W')
        self.chkbtnInputVisceraWeight.grid(row=3, column=3, sticky='W')
        self.chkbtnInputShellWeight.grid(row=4, column=1, sticky='W')
        self.chkbtnInputRings.grid(row=4, column=2, sticky='W')

        # Datos atipicos, ubicacion en el grid y definicion del comando de ejecucion para el boton

        self.atypicalLabel.grid(row=5, column=0, columnspan=2, sticky='NW', pady=15)

        self.atypicalInput.grid(row=5, column=2, sticky='W', padx=10)

        self.btnAtypical.grid(row=5, column=3, pady=15)
        self.btnAtypical.config(command=self.removeAtypics)

        # Variables de entrada y campos de seleccion para la regresion - Ubicacion en el grid

        self.regressionLabel.grid(row=6, column=0, sticky='W')

        self.chkbtnInputRegressionLenght.grid(row=6, column=1, sticky='W')
        self.chkbtnInputRegressionDiameter.grid(row=6, column=2, sticky='W')
        self.chkbtnInputRegressionHeight.grid(row=6, column=3, sticky='W')
        self.chkbtnInputRegressionWholeWeight.grid(row=7, column=1, sticky='W')
        self.chkbtnInputRegressionShuckedWeight.grid(row=7, column=2, sticky='W')
        self.chkbtnInputRegressionVisceraWeight.grid(row=7, column=3, sticky='W')
        self.chkbtnInputRegressionShellWeight.grid(row=8, column=1, sticky='W', pady=(0,15))
        self.chkbtnInputRegressionRings.grid(row=8, column=2, sticky='W', pady=(0,15))

        # Variables de salida y campos de seleccion para la regresion - Ubicacion en el grid

        self.regressionLabel.grid(row=9, column=0, sticky='W')
        self.chkbtnOutputRegressionLenght.grid(row=9, column=1, sticky='W')
        self.chkbtnOutputRegressionDiameter.grid(row=9, column=2, sticky='W')
        self.chkbtnOutputRegressionHeight.grid(row=9, column=3, sticky='W')
        self.chkbtnOutputRegressionWholeWeight.grid(row=10, column=1, sticky='W')
        self.chkbtnOutputRegressionShuckedWeight.grid(row=10, column=2, sticky='W')
        self.chkbtnOutputRegressionVisceraWeight.grid(row=10, column=3, sticky='W')
        self.chkbtnOutputRegressionShellWeight.grid(row=11, column=1, sticky='W')
        self.chkbtnOutputRegressionRings.grid(row=11, column=2, sticky='W')

        # Definicion del comando a ejecutar para el boton de realizar la regresion y ubicacion en el grid

        self.btnregression.grid(row=12, column=1, sticky='WE', padx=5, pady=10)

        # Definicion del comando a ejecutar para el boton de graficar y bicacion en el grid

        self.btngraph.grid(row=12, column=2, sticky='WE', padx=5, pady=10)
        self.btngraph.config(command=self.graph)

    # Metodo de generacion de ventana emergente para mostrar alertas u errores

    def errorWindow(self, title, message):
        newgraphWindow = tk.Toplevel(self.root)
        newgraphWindow.resizable(False, False)
        newgraphWindow.title(title)
        
        frame = tk.Frame(newgraphWindow, width='1080', height='650')
        frame.pack()
        frame['bg'] = '#faf9f9' 
        
        lbl = tk.Label(frame, text=message, bg='#faf9f9', font=(16))
        lbl.grid(row=0)
        
        btnClose = tk.Button(frame, text="Cerrar", activeforeground='#faf9f9', activebackground='#555B6E', fg='#faf9f9', bg='#555B6E', cursor='hand2', command=lambda: newgraphWindow.destroy())
        btnClose.grid(row=1, pady=10)
    
    # Metodo de identificacion de las variables seleccionadas

    def checkSelectedInput(self):
        selectedInput = []
        
        if self.varInputLenght.get() == 1:
            selectedInput.append('Length')
        if self.varInputDiameter.get() == 1:
            selectedInput.append('Diameter')
        if self.varInputHeight.get() == 1:
            selectedInput.append('Height')
        if self.varInputWholeWeight.get() == 1:
            selectedInput.append('Whole weight')
        if self.varInputShuckedWeight.get() == 1:
            selectedInput.append('Shucked weight')
        if self.varInputVisceraWeight.get() == 1:
            selectedInput.append('Viscera weight')
        if self.varInputShellWeight.get() == 1:
            selectedInput.append('Shell weight')
        if self.varInputRings.get() == 1:
            selectedInput.append('Rings')
        
        return selectedInput

    # Metodo de graficacion de los datos

    def graph(self):
        

        selectedInput = self.checkSelectedInput()
        incoherence = False

        if (len(selectedInput) == 1):

            if (self.comboGraphs.get() == 'Histograma'):
                plot.hist(self.dataSetObject.data[selectedInput[0]])

            elif (self.comboGraphs.get() == 'Diagrama de caja'):
                plot.boxplot(self.dataSetObject.data[selectedInput[0]])

            elif (self.comboGraphs.get() == 'Normalización'):
                graph = plot.figure()
                ax = graph.add_subplot(111)
                stats.probplot(self.dataSetObject.data[selectedInput[0]], dist=stats.norm, sparams=(6,), plot=ax)
            
            else:
                incoherence = True

        elif (len(selectedInput) == 2):

            if (self.comboGraphs.get() == 'Dispersión'):
                plot.scatter(self.dataSetObject.data[selectedInput[0]], self.dataSetObject.data[selectedInput[1]])

            else:
                incoherence = True
    
        if incoherence == True:
            self.errorWindow('Error',f'Recuerda, para realizar un histograma, un diagrama de caja o un gráfico de normalización se requiere \n únicamente que tengas una variable de entrada seleccionada, pero, para realizar un gráfico de dispersión \n se requiere que tengas dos variables de entrada seleccionadas.')
            return

        plot.title(self.comboGraphs.get())
        plot.xlabel('Valor de los datos')
        plot.ylabel('Cantidad de los datos')
        plot.show()

    # Metodo para eliminar los datos atipicos
    
    def removeAtypics(self):
        
        if (self.btnAtypical['text'] == 'Eliminar atípicos'):

            alpha = self.atypicalInput.get()

            maxlimits = []
            minlimits = []
            
            try:
                for i in range (1, len(self.dataSetObject.data.columns)):
                    q75 = np.quantile(self.dataSetObject.data[self.dataSetObject.data.columns[i]],.75)
                    q25 = np.quantile(self.dataSetObject.data[self.dataSetObject.data.columns[i]],.25)
                    intr_qr = q75 - q25

                    maxlimits.append(q75 + (float(alpha) * intr_qr))
                    minlimits.append(q25 - (float(alpha) * intr_qr))

                self.dataSetObject.data = self.dataSetObject.copyData[(self.dataSetObject.copyData['Length'] < maxlimits[0]) & (self.dataSetObject.copyData['Length'] > minlimits[0]) & (self.dataSetObject.copyData['Diameter'] < maxlimits[1]) & (self.dataSetObject.copyData['Diameter'] > minlimits[1]) & (self.dataSetObject.copyData['Height'] < maxlimits[2]) & (self.dataSetObject.copyData['Height'] > minlimits[2]) & (self.dataSetObject.copyData['Whole weight'] < maxlimits[3]) & (self.dataSetObject.copyData['Whole weight'] > minlimits[3]) & (self.dataSetObject.copyData['Shucked weight'] < maxlimits[4]) & (self.dataSetObject.copyData['Shucked weight'] > minlimits[4]) & (self.dataSetObject.copyData['Viscera weight'] < maxlimits[5]) & (self.dataSetObject.copyData['Viscera weight'] > minlimits[5]) & (self.dataSetObject.copyData['Shell weight'] < maxlimits[6]) & (self.dataSetObject.copyData['Shell weight'] > minlimits[6]) & (self.dataSetObject.copyData['Rings'] < maxlimits[7]) & (self.dataSetObject.copyData['Rings'] > minlimits[7])]
                self.errorWindow('Solicitud exitosa', 'La remosión de los datos atípicos se ha realizado de manera exitosa')
                self.btnAtypical['text'] = 'Restaurar atípicos'

            except:
                self.errorWindow('Error','Ups, algo ha salido mal, revisa que el valor de alpha sea valido')
                return

        else:

            self.dataSetObject.data = self.dataSetObject.copyData.copy()
            self.errorWindow('Solicitud exitosa', 'La restauración de los datos atípicos se ha realizado de manera exitosa')
            self.btnAtypical['text'] = 'Eliminar atípicos'
        

        self.atypicalInput.delete(0,END)

# Llamado a la accion de la aplicacion

if __name__ == "__main__":
    app = main()
    app.root.mainloop()